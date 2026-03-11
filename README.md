# DKMap <a href="https://github.com/DKMap-VIS/DKMap" style="color: #65513C; font-family: 'Maiden Orange', sans-serif; font-weight: bold;"></a>

A novel DR visualization technique for interactive exploration of multimodal embeddings through Dynamic Kernel enhanced projection


<table>
  <tr>
    <td colspan="3"><video width="100%" src='https://github.com/user-attachments/assets/1eeec725-dd91-464d-9e47-42374c24cd48'>Web-based</td>
    <td colspan="3"><video width="100%" src='https://github.com/user-attachments/assets/647ba1b2-6c75-4554-a0f1-0c48ce1a2c6f'>Colab</td>
  </tr>
  <tr></tr>
</table>


## What is DKMap about?
DKMap helps you make sense of multimodal embeddings — especially those from vision-language models — by showing how well text and images align. Traditional methods like t-SNE often fail to accurately reflect alignment metrics due to projection distortion and over-averaging. DKMap solves this with a dynamic kernel approach that makes the visualizations both more accurate and more interactive. You can zoom in, explore local details, and use it in your browser or Jupyter notebook.

## Highlights
✨ Scalable to <strong>billions</strong> of <strong>multimodal embedding</strong> point

✨ Enables <strong>multi-resolution</strong> exploration via kernel
refinement

✨ Dynamically adjusts the granularity of the contour map for more flexible exploration.

✨ Support multi-platform development -- <strong>computational notebooks</strong> (e.g., Colab, Jupyter, VS Code) and <strong>Web-based system</strong>


## Quick Start

### Data

We provide prepared embedding files list here: 
- [DiffusionDB](https://drive.google.com/drive/folders/1w5fpg0dLDrsQ_VhGge2uzcS-cOcnGXhu?usp=sharing)
- [Pick-a-Pic](https://drive.google.com/drive/folders/1mz79GBRaBDKIUhrkWj1-l_LUUKacQBey?usp=sharing)


### Web-based system
Clone or download this repository:
```bash
git clone https://github.com/DKMap-VIS/DKMap.git
```
Install the dependencies (in the Backend folder):
```bash
pip install -r requirements.txt
```
Install the dependencies (in the Frontend folder):
```bash
npm install
```
#### Path Modification (Required Before Running)
Please update the file paths in the following code file according to your local environment.
- File：```app.py```
     - line 35: (a .csv file) included position, alignment metric, image path and prompt of all data points.
     - line 53: (a .npy file) included your data embedding.

- File: ```Main.vue```
     - line 345: (.csv files) included contour map values.
     - line 53: (a .csv file) included position, alignment metric, image path and prompt of all data points.

Then run DKMap:
```bash
npm run dev
```

### Python package
Download the source code from the Python package file.

#### 🚀Notice
- Most parameters are loaded automatically from ```config.yaml```.
- If you want to use this package in your own project, you need to manually pass the following parameters to the main function:
   - points_ds: dataset embedding (a .npy file)
   - input_dimens: input feature dimension
   - scores: alignment metric embedding (a .npy file)
- Alternatively, you can follow the steps in our provided ```Projection_and_mapping.ipynb```, which demonstrates how to train a projection and mapping model and generate a static projection map.
- For further interactive exploration of the dataset, please refer to ```Interactive_contour_visualization.ipynb```.


## Citation

```bibtex
@ARTICLE{ye2026DKMap,
  author={Ye, Yilin and Ruan, Chenxi and Zhang, Yu and Deng, Zikun and Zeng, Wei},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={{DKMap}: Interactive Exploration of Vision-Language Alignment in Multimodal Embeddings via Dynamic Kernel Enhanced Projection}, 
  year={2026},
  volume={32},
  number={1},
  pages={440-450},
  doi={10.1109/TVCG.2025.3642641}
}
```




