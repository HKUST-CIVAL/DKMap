from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

import os
import numpy as np
# import clip
from scipy.optimize import direct, Bounds

import torch
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

from scipy.spatial.distance import euclidean
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import DictionaryLearning
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler

from collections import Counter
import open_clip
import faiss
import pandas as pd

#load CLIP model
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
clip_model, preprocess, preprocess_val = open_clip.create_model_and_transforms('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')

clip_model.cuda().eval()


from keybert import KeyBERT

df = pd.read_csv('hps_diffusiondb_merged2.csv') # your_file_path
image_paths = df['im_path'].tolist() 

app = Flask(__name__)
CORS(app)
FILE_ABS_PATH = os.path.dirname(__file__)

@app.route('/api/test/hello/', methods=['POST'])
def hello_resp():
    params = request.json
    return "hello VUE"

@app.route('/api/test/analyze-prompts/', methods=['POST'])
def analyze_prompts():
    data = request.json
    prompts = data.get("prompts", [])
    index = data.get("index",[])

    embeddings = np.load('txt_emb_diffusiondb_hps.npy') # your_file_path
    selected_embeddings = []
    # selected_img = []
    for id in index:
        id = int(id)
        selected_embeddings.append(embeddings[id-1])  

    selected_embeddings = np.array(selected_embeddings)

    def extract_keywords_bert(text, max_words=1, top_n=5):
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, max_words), top_n=top_n)
        return [kw[0] for kw in keywords]
    
    def filter_keywords(keywords):
        unique_keywords = []
        for keyword in keywords:
            # 保证不添加包含关系重复的关键词
            if not any(keyword in unique or unique in keyword for unique in unique_keywords):
                unique_keywords.append(keyword)
        return unique_keywords

    all_keywords = []
    for text in prompts:
        keywords = extract_keywords_bert(text)
        unique_keywords = filter_keywords(keywords)
        all_keywords.extend(unique_keywords)

    # 统计关键词频率，取前 15
    keyword_counts = Counter(all_keywords)
    top_keywords = [kw[0] for kw in keyword_counts.most_common(15)]
    top_counts = [kw[1] for kw in keyword_counts.most_common(15)]
    print(top_counts)
    keyword_similarities = {}
    def normalize_keyword_similarities(keyword_similarities):
        """归一化每个关键词的相似度到 [0, 1]"""
        scaler = MinMaxScaler(feature_range=(0, 1))
        for keyword in keyword_similarities:
            similarities = np.array(keyword_similarities[keyword]).reshape(-1, 1)
            keyword_similarities[keyword] = list(scaler.fit_transform(similarities).flatten())
        return keyword_similarities

    for keyword in top_keywords:
        text_input = tokenizer([keyword]).to(DEVICE)
        keyword_similarities[keyword] = []
        with torch.no_grad():
            word_embedding = clip_model.encode_text(text_input).cpu().numpy().flatten()
        for text_embedding in selected_embeddings:
            similarity = float(cosine_similarity([word_embedding], [text_embedding]).flatten()[0])
            keyword_similarities[keyword].append(similarity)

    normalized_keyword_similarities = normalize_keyword_similarities(keyword_similarities)

    return normalized_keyword_similarities

@app.route('/api/test/get-data/', methods=['GET'])
def get_data():
    """Return dataset information as JSON"""
    try:
        # Check if DataFrame is loaded
        if df is None or df.empty:
            return jsonify({'error': 'Dataset not loaded'}), 500
        
        # Convert DataFrame to JSON-serializable format
        data = {
            'positions': [],
            'prompts': [],
            'image_paths': [],
            'indices': []
        }
        
        # Safely extract columns with existence checks
        if 'x' in df.columns and 'y' in df.columns:
            data['positions'] = df[['x', 'y']].values.tolist()
        else:
            print("Warning: 'x' or 'y' column not found in CSV")
            print("Available columns:", df.columns.tolist())
        
        if 'prompt' in df.columns:
            data['prompts'] = df['prompt'].fillna('').tolist()
        else:
            print("Warning: 'prompt' column not found in CSV")
            data['prompts'] = [''] * len(df)
        
        if 'im_path' in df.columns:
            data['image_paths'] = df['im_path'].fillna('').tolist()
        else:
            print("Warning: 'im_path' column not found in CSV")
            data['image_paths'] = [''] * len(df)
        
        data['indices'] = df.index.tolist()
        
        print(f"Dataset loaded: {len(data['positions'])} positions, {len(data['prompts'])} prompts")
        
        return jsonify(data)
    
    except Exception as e:
        print(f"Error in get_data: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/test/similar-search/', methods=['POST'])
def find_similar_images():
    data = request.json
    selected_image_names = int(data.get("index",[]))
    print(selected_image_names)

    index = faiss.read_index('image_index_diffusiondb_hps.index') # your_file_path
    embeddings = np.load('img_emb_diffusiondb_hps.npy') # your_file_path


    features = embeddings[selected_image_names-1]

    top_k = data.get('topK', 11)
    D, I = index.search(features.reshape(1, -1), top_k) 
    
    # 返回最相似图片的路径
    similar_images = [image_paths[i] for i in I[0]]
    
    return jsonify(similar_images)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
