<template>
    <div style="background-color: #edf1f5; width:100%;height:100%">
        <el-row>
            <!-- <el-col :span="1"></el-col> -->
            <el-col :span="10">
                <div style="width:2180px;height:30px;margin-left:250px;background-color: #B8ADAE;">

                </div>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="1">
                <div id="ModelPanel"
                    style="width:372px;height:1160px;margin-left:250px;background-color: white;border-radius: 8px;margin-top:5px">
                    <div id="title" style="width:370px;height:220px;overflow: hidden;">
                        <h1 class="maiden-orange-regular" style="margin-left: -5px;margin-top: -25px;">DKMap</h1>
                        <div class="content" style="width:90%;margin-left:7%;margin-top: -25px;">
                            <p style="font-size: 14px;font-weight: bold;text-align: left;font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif">An interactive system for exploring vision-language alignment in multimodal embeddings.</p>
                        </div>
                    </div>
                    <div class="header2" style="width:96%;margin-left:2%;">
                        <p style="font-size: 18px;font-weight: bold;">Settings</p>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">
                        <div style="width: 10px; height: 20px; background-color: black;margin-left:25px;"></div>
                        <p style="font-size: 24px; font-weight: bold;">Dataset</p>
                    </div>
                    <div id="dataset" style="width:370px;height:60px;">
                        <div class="rectangle" style="margin-left: 40px;margin-top: 20px;">
                            <span>{{ selectedOption || "Select a dataset" }}</span>
                            <!-- <span>Select the dataset</span> -->
                            <button class="svg-button" @click="toggleDropdown">
                                <svg width="12" height="7" viewBox="0 0 12 7" fill="none" xmlns="http://www.w3.org/2000/svg"> 
                                    <path d="M11 1L6 6L1 1" stroke="#1C274C" stroke-opacity="0.6" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> 
                                </svg>
                            </button>
                            
                        </div>
                        <div v-if="isOpen" class="dropdown">
                            <div>
                                <p @click="selectOption('DiffusionDB 2M')" class="dropdown-item">DiffusionDB 2M</p>
                                <!-- <p @click="selectOption('SDXL(MSCOCO captions)')" class="dropdown-item">SDXL(MSCOCO captions)</p>
                                <p @click="selectOption('SD3(MSCOCO captions)')" class="dropdown-item">SD3(MSCOCO captions)</p>
                                <p @click="selectOption('Pick-a-pic')" class="dropdown-item">Pic-a-pick</p>
                                <p @click="selectOption('MSCOCO')" class="dropdown-item">MSCOCO</p> -->
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">
                        <div style="width: 10px; height: 20px; background-color: black;margin-left:25px;"></div>
                        <p style="font-size: 24px; font-weight: bold;">Dataset Details</p>
                    </div>
                    <div id="datasetdetails" style="width:300px;height:250px;text-align: left;margin-left: 45px;padding-top: 10px;">
                        <div v-if="selectedOption">
                            <p><strong>Num of Images:</strong> {{ datasetDetails.numImages }}</p>
                            <p><strong>Num of Unique Prompts:</strong> {{ datasetDetails.numPrompts }}</p>
                            <p><strong>Size:</strong> {{ datasetDetails.size }}</p>
                            <p><strong>Language:</strong> {{ datasetDetails.language }}</p>
                        </div>
                    </div>

                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">
                        <div style="width: 10px; height: 20px; background-color: black;margin-left:25px;"></div>
                        <p style="font-size: 24px; font-weight: bold;">Metric Selection</p>
                    </div>
                    <div id="metricdetails" style="width:370px;height:420px;display: flex;flex-direction: column;">
                        <div class="buttons">
                            <button 
                                v-for="(button, index) in buttonList" 
                                :key="index" 
                                class="rectangle-button" 
                                :class="{ active: selectedButton === button.name }"
                                @click="selectButton(button.name, button.description)"
                            >
                                {{ button.name }}
                            </button>
                        </div>
                        <div class="explanation" style="width:300px;height:260px;border-radius: 10px;border: 2.5px solid rgba(44, 62, 80, 0.6);margin-top: 29px;text-align: left;padding: 6px;font-size: 17px;margin-left: 35px;">
                            <p v-if="selectedText">{{ selectedText }}</p>
                        </div>

                    </div>




                    <!-- border: 2px solid black; -->
                   
                </div>
            </el-col>

            <el-col :span="14">
                <div id="TestPrompt"
                    style="width:1180px;height:1160px;margin-left:525px;background-color: white;border-radius: 8px;margin-top:5px">

                    <div class="header2" style="width:96%;margin-left:2%;">
                        <p style="font-size: 18px;font-weight: bold;">Overview</p>
                    </div>

                    <br>
                    <br>
                    <!-- border: 2px solid black; -->
                   
                    <div id="overview" style="width:1300px;height:900px;left: -60px;margin-top:-10px;">
                    
                        <div style="width:40px;height:300px;display: inline-block;float:left">
                            <p style="margin-left:67px;font-size: 18px;margin-top: 5px;">Lasso</p>
                            <el-button id="select_align_button" @click="select()"
                                style="width:50px;height:50px;margin-left:66px;" :type="alignButtonType">
                                <el-icon :size="40" style="vertical-align: middle">
                                    <Operation />
                                </el-icon>
                            </el-button>
                            <p style="margin-left:69px;font-size: 18px;margin-top: 5px;">Mode</p>
                            <el-button id="select_align_button" @click="setPoint()"
                                style="width:50px;height:50px;margin-left:66px;" :type="contourType">
                                <el-icon :size="40" style="vertical-align: middle">
                                    <View />
                                </el-icon>
                            </el-button>


                        </div>




                    </div>
                </div>
            </el-col>
            <el-col :span="4">
                <div id="Disentangle"
                    style="width:595px;height:1160px;background-color: white;border-radius: 8px;margin-top:5px;margin-left:155px">

                    <div class="header" style="width:94%;margin-left: 3%;">
                        <p style="font-size: 18px;font-weight: bold;">Keyword Distribution View</p>
                    </div>
                    <div id="augview" style="width:590px;height:640px;overflow: hidden;">

                        <div id="graph-container" style="width: 550px; height: 635px; margin-top: 10px; margin-left: 35px;display: flex;
                        flex-wrap: wrap;justify-content: left;gap:7px;overflow-y: auto;">
                           
                        </div>

                    </div>
                    <!-- justify-content: center; -->
                    <div class="header2" style="width:94%;margin-left: 3%;margin-top: 5px;">
                        <p style="font-size: 18px;font-weight: bold;">Instance View</p>
                    </div>
                    <div id="graph-container" style="width: 630px; height: 500px; margin-top: 5px; margin-left: 10px; display: flex;flex-direction: column; ">
                        <div id="main-image-container" style="overflow-y: auto;  width: 490px;display: flex; flex-direction: row; margin-left: 35px;height: 160px;">
                            <img id="imageDisplay" src="" style="display:none; width: 150px;height:150px; margin-top: 10px;object-fit: fill;margin-left: 15px; ">
                            <div style="display: flex; flex-direction: column; justify-content: center; margin-left: 65px;margin-top: 10px;">
                                <p id="Score" style="font-size: 17px; font-weight: bold;text-align: left;"></p>
                                <p id="scoreSimilarity" style="font-size: 16px; text-align: left;"></p>
                                <p id="defaultCaption" style="font-size: 17px; font-weight: bold;text-align: left;"></p>
                                <p id="promptDisplay" style="font-size: 16px; width: 250px; word-wrap: break-word;text-align: left;height: 100px;overflow-y: auto;"></p>
 

                            </div>
                        </div>
                        <p style="font-size: 14px;font-weight: bold;width:94%;margin-top: 30px;">Similar Samples from Dataset</p>
                        <div id="image-thumbnails" style="display: flex; flex-wrap: wrap; gap: 12px; width: 500px;justify-content: center;margin-left: 37px;margin-top: 10px;;">

                        </div>
                    </div>
                    
                </div>

            </el-col>
        </el-row>


    </div>
</template>

<script>
import * as d3 from 'd3'
import * as echarts from 'echarts';
import {transform} from 'echarts-stat';
import * as ecStat from 'echarts-stat';
import * as Plotly from 'plotly.js-dist';
import 'd3-lasso'

import axios from 'axios';


export default {
    name: 'APP',
    props: ["msgH"],
    data() {
        return {
            msg1: "Hello, main!",
            moreSearch: -1,
            formData1: {
                name: '',

            },
            formData2: {
                name: '',

            },
            isCanvasInteractive: false, 
            showPoint:true,
            newSelectedPoints:[],
            highlightedPoint:null,
            drawnRectangles:[],
            isOpen: false,
            selectedOption: 'Select the dataset',
            selectedButton: null, // 记录选中的按钮
            selectedText: "", // 选中的解释文本
            buttonList: [
                // { name: "CLIPScore", description: "CLIPScore is an evaluation metric that measures the semantic similarity between images and text using CLIP. It is commonly used to assess how well a textual description matches a given image without relying on human-annotated reference texts." },
                // { name: "MPS", description: "MPS is a CLIP-based evaluation metric that assesses text-to-image generation quality across four key dimensions - aesthetics, text alignment, detail quality, and overall preference - using conditional masking to dynamically weight these factors for more nuanced feedback than single-score metrics." },
                { name: "HPSv2", description: "HPSv2 is a robust evaluation metric for text-to-image generation that predicts human preferences by fine-tuning CLIP on 798K carefully annotated image comparisons." },
                // { name: "PickScore", description: "PickScore is a real-user preference predictor trained on over 500K natural rankings that outperforms human annotators (70.5% accuracy) in selecting preferred images, making it particularly valuable for practical applications like ranking multiple model outputs." }
            ],
            datasetInfo: {
                "DiffusionDB 2M": { numImages: "2M", numPrompts: "1.5M", size: "1.6T", language: "Mostly English and other languages such as Spanish, Chinese, and Russian." },
                // "SDXL(MSCOCO captions)": { numImages: "10M", numPrompts: "8M", size: "500GB", language: "Multilingual" },
                // "Pick-a-pic": { numImages: "10M", numPrompts: "8M", size: "500GB", language: "Multilingual" },
                // "MSCOCO": { numImages: "5B", numPrompts: "3B", size: "10TB", language: "Multilingual" },

            }
        }
    },
    computed: {
        datasetDetails() {
            return this.datasetInfo[this.selectedOption] || {};
        }
    },
    methods: {
        selectButton(name, description) {
            this.selectedButton = name;
            this.selectedText = description;
            if(name=="HPSv2")
                this.drawAlignmentMap(); 
        },
        selectOption(option) {
            this.selectedOption = option;  
            this.isOpen = false; 
        },
        toggleDropdown(option) {
            this.isOpen = !this.isOpen;
            // console.log('按钮点击了！');
        },
        debrush() {
            d3.select("#matrixGr").call(d3.brush().extent([[0, 0], [0, 0]]))
        },
        setPoint(){
            this.showPoint = !this.showPoint;
            const canvas = document.querySelector("canvas"); // 获取 canvas
            if (canvas) {
                canvas.style.display = this.showPoint ? "block" : "none"; 
            }
        },

        select(){
            const canvas = document.querySelector("canvas"); // 获取 canvas
            if (!canvas) return;

            this.isCanvasInteractive = !this.isCanvasInteractive;
            canvas.style.pointerEvents = this.isCanvasInteractive ? "auto" : "none";

            console.log("Canvas:", canvas.style.pointerEvents);

        },

        drawPoints(data2,context,transform){
            context.clearRect(0, 0, 1025, 1025);
                // console.log("clean",currentGridSize)
            // let grid = Math.max(1, Math.floor(1024 / 32));
            let grid = Math.max(1, Math.floor(1024 / 16));
                // console.log(grid)
                // console.log("width",canvas.width)
                // console.log(transform.x,transform.y)
            let zoomCenterX = (1025 / 2 - transform.x) / transform.k;
            let zoomCenterY = (1025 / 2 - transform.y) / transform.k;
            let extent = d3.extent(data2.map(d => d.score)); 
                // console.log(extent)
                // console.log(extent[0])
            // console.log(extent[1])
            let color = d3.scaleSequential(d3.interpolateRdYlBu).domain([0.3278125, 0.19]);
            // console.log("data2",data2)
            data2.forEach((d, i) => {
                // coco
                // let x = (grid+5)*(parseFloat(d["x"]))+530;
                // let y = (grid+31)*(-parseFloat(d["y"]))+480;
                let x = (grid+10)*(parseFloat(d["x"]))+402;
                let y = (grid+5.78)*(-parseFloat(d["y"]))+490;
                // let x = (grid-2)*(parseFloat(d["x"]))+560;
                // let y = (grid-3.5)*(-parseFloat(d["y"]))+435;

                // 计算相对画布中心的偏移
                let dx = x - zoomCenterX;
                let dy = y - zoomCenterY;

                x = 1025 / 2 + dx * transform.k;
                y = 1025 / 2 + dy * transform.k;

                let radius = 3
                if(this.highlightedPoint && d["im_path"] === this.highlightedPoint.im_path)
                    radius = 8

                context.fillStyle = color(d["score"]);
                context.strokeStyle = "rgba(128, 128, 128, 0.5)";
                context.lineWidth = 0.6; // 边框宽度

                        // 绘制圆形（点）
                context.beginPath();
                // context.fillRect(x - radius, y - radius, 2*radius, 2*radius);

                context.arc(x, y, radius, 0, 2 * Math.PI); // 绘制圆
                context.fill(); // 填充颜色
                context.stroke(); // 绘制边框
            });
            // console.log("1",this.drawnRectangles)
            if(this.drawnRectangles.length){
                context.strokeStyle = "black";
                context.strokeRect(this.drawnRectangles[0].x, this.drawnRectangles[0].y, this.drawnRectangles[0].width, this.drawnRectangles[0].height);
            }

        },

        async drawAlignmentMap() {
            let width = 1025
            let height = 1025
            let size = 1024

            let svg = d3.select("#overview").append("svg")
                .attr("id", "classOverviewSvg")
                .attr("width", width)
                .attr("height", height)
                .style("overflow", "hidden")
                .append("g").attr("id", "classOverviewGr")

            let contourGroup = svg.append("g")

            let viewX = 0, viewY = 0, viewSize = 512;
            let currentZoomLevel = 1;
            let label = 1;
            let currentGridSize = 64;
         
            const contourFiles = {
                1: "/contour_values_hps64.csv",
                2: "/contour_values_hps256.csv",
                3: "/contour_values_hps1024.csv",
                4: "/contour_values_hps1024k2.csv",
                5: "/contour_values_hps1024k4.csv",
                6: "/contour_values_hps1024k6.csv",
                7: "/contour_values_hps1024k8.csv",

            };

            let quadtree = {};

            // 加载所有等高线数据
            async function loadAllContours() {
                for (let key in contourFiles) {
                    let label = parseInt(key);
                    let text = await d3.text(contourFiles[key]);  
                    let data = d3.csvParseRows(text, row => row.map(Number));  
                    quadtree[label] = data;
                }
                console.log("四叉树初始化完成", quadtree);
            }

            let data1 = await d3.csv("/hps_diffusiondb_merged.csv");

            await loadAllContours(); 

            console.log("here")

            let sampleSize = 10000

            let indices = data1.map((_, i) => i);

            // Shuffle the indices using Fisher-Yates Shuffle
            for (let i = indices.length - 1; i > 0; i--) {
                let j = Math.floor(Math.random() * (i + 1)); // Pick a random index up to i
                [indices[i], indices[j]] = [indices[j], indices[i]]; // Swap elements
            }

            // Select the first `sampleSize` indices
            let sampledIndices = indices.slice(0, sampleSize);

            // Slice the array based on the sampled indices
            let data2 = sampledIndices.map(i => data1[i]);
            // let extent1 = d3.extent(data1.map(d => d.score)); 
            // console.log("ex",extent1)
            // console.log(data2)

            let initPoints = data2;

            data1.forEach((d, i) => {
                d.scaleLevel = i % 500+1; 
            });

            const container = document.getElementById("overview");

            const canvas = document.createElement("canvas");
            canvas.width = width;
            canvas.height = height;
            container.appendChild(canvas);
            canvas.style.position = "absolute"; 
            canvas.style.left = "156px";  
            canvas.style.top = "0px"; 
            canvas.style.pointerEvents = "none";  
            const context = canvas.getContext("2d");
            let defaultTransform = { x: 0, y: 0, k: 1 };
            let currentTransform= { x: 0, y: 0, k: 1 };
            const canvasCenterX = canvas.width / 2;
            const canvasCenterY = canvas.height / 2;

            // canvas.width = 4100;
            // canvas.height = 4100;
            // canvas.style.width = "1025px";
            // canvas.style.height = "1025px";

            // context.scale(4, 4);


            function drawContours(label,gridSize, domainx, domainy) {
                console.log("label",label)
                let score_array = quadtree[label]
                let x = d3.scaleLinear([0, 1], [0, 512])
                let y = d3.scaleLinear([0, 1], [0, 512])
                let q = Math.max(1, Math.floor(1024 / gridSize)); // The level of detail, e.g., sample every 4 pixels in x and y.
                // let x0 = -q / 2, x1 = 500 + q;
                // let y0 = -q / 2, y1 = 500 + q;
                let x0 = q / 2, x1 = 512 + q;
                let y0 = q / 2, y1 = 512 + q;
                let n = gridSize;
                let m = gridSize;
                let grid = new Array(n * m);
                // console.log(n)
                // console.log(m)
                for (let j = 0; j < m; ++j) {
                   for (let i = 0; i < n; ++i) {
                        grid[(n - i - 1) * m + j] = score_array[i][j];
                    }
                }
                grid.x = -q;
                grid.y = -q;
                grid.k = q;
                grid.n = n;
                grid.m = m;

                let min_end = 25
                let extent = d3.extent(score_array.flat()); // Find min and max

                let thresholds = d3.range(extent[0], extent[1], (extent[1] - extent[0]) / 40);
                let color = d3.scaleSequential(d3.interpolateRdYlBu).domain([extent[1], extent[0]]);


                let transform = ({ type, value, coordinates }) => {
                    return {
                        type, value, coordinates: coordinates.map(rings => {
                            return rings.map(points => {
                                return points.map(([x, y]) => ([
                                    grid.k * x,
                                    grid.k * y
                                ]));
                            });
                        })
                    };
                }

                let contours = d3.contours()
                    .size([grid.n, grid.m])
                    .thresholds(thresholds)
                    (grid)
                    .map(transform)

                contourGroup.selectAll("path").remove();

                contourGroup.append("g")
                    .attr("fill", "none")
                    // .attr("stroke", "#fff")
                    .attr("stroke-opacity", 0.5)
                    .selectAll("path")
                    .data(contours)
                    .join("path")
                    .attr("fill", (d) => {
                        const res = color(d.value)
                        return res
                    }
                    )
                    .attr("fill-opacity", 0.3)
                    .attr("d", d3.geoPath())
                    // .attr("stroke", "black")
                    .style("mix-blend-mode", "normal") //为了不重叠
                    .transition()
                    .duration(100) 
                    .ease(d3.easeLinear) 

                    
            }

            const hoverRadius = 8; 
            const fibonacciLevels = [0, 1, 2, 3, 5, 8, 13, 21, 21, 34, 34, 55, 55,55,55,64];
            let isDrawing = false;
            let isSelecting = false;
            let rectStartX, rectStartY;
            let rectWidth, rectHeight;
            let selectedPoints = [];

            canvas.addEventListener("mousemove", (event)=> {
                if (canvas.style.pointerEvents === "auto") {
                let rect = canvas.getBoundingClientRect();
                let mouseX = event.clientX - rect.left;
                let mouseY = event.clientY - rect.top;

                let foundPoint = null;
                // console.log("succeed")
                let zoomCenterX = (canvas.width / 2 - currentTransform.x) / currentTransform.k;
                let zoomCenterY = (canvas.height / 2 - currentTransform.y) / currentTransform.k;

                // 检测每个点是否在鼠标悬浮的范围内
                for (let d of data2) {
                    let grid = Math.max(1, Math.floor(1024 / 16));
                    // let x = (grid+5)*(parseFloat(d["x"]))+530;
                    // let y = (grid+31)*(-parseFloat(d["y"]))+480;
                    let x = (grid+10)*(parseFloat(d["x"]))+402;
                    let y = (grid+5.78)*(-parseFloat(d["y"]))+490;
                    // let x = (grid-2)*(parseFloat(d["x"]))+560;
                    // let y = (grid-3.5)*(-parseFloat(d["y"]))+435;

                    let dx1 = x - zoomCenterX;
                    let dy1 = y - zoomCenterY;

                    x = canvasCenterX + dx1 * currentTransform.k;
                    y = canvasCenterY + dy1 * currentTransform.k;

                    let dx = x - mouseX;
                    let dy = y - mouseY;
                    let distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < hoverRadius) { // 如果鼠标在点的范围内
                        foundPoint = d;
                        break;
                    }
                }

                // 如果找到了新的点，更新 `highlightedPoint` 并重新绘制
                if (!this.highlightedPoint){
                    this.highlightedPoint = foundPoint;
                    if(!this.newSelectedPoints.length){
                        this.drawPoints(data2, context, currentTransform);
                        // console.log("transform")
                    }
                    else
                        this.drawPoints(this.newSelectedPoints, context, currentTransform);
                }
                if(this.highlightedPoint && foundPoint){
                    if (foundPoint["im_path"] !== this.highlightedPoint.im_path) {
                        this.highlightedPoint = foundPoint;
                        console.log("highlight", this.highlightedPoint)
                        if(!this.newSelectedPoints.length){
                            this.drawPoints(data2, context, currentTransform);
                            // console.log("transform")
                        }
                        else
                            this.drawPoints(this.newSelectedPoints, context, currentTransform);
                        
                    }

                }


            }
            });

            canvas.addEventListener("mouseleave", (event)=> {
                this.highlightedPoint = null;
                if(!this.newSelectedPoints.length){
                    this.drawPoints(data2,context,currentTransform);
                    console.log("found2")
                    console.log("2",this.drawnRectangles)
                }
                else
                    this.drawPoints(this.newSelectedPoints, context, currentTransform);
                    
                    
            });

            canvas.addEventListener("click", async (event) => {
                console.log(isSelecting+"click");
                if(isSelecting)return;
                if (canvas.style.pointerEvents === "auto") {
                    let rect = canvas.getBoundingClientRect();
                    // console.log(rect)
                    let mouseX = event.clientX - rect.left;
                    let mouseY = event.clientY - rect.top;

                    let clickedPoint = null;

                    // 计算缩放中心
                    let zoomCenterX = (canvas.width / 2 - currentTransform.x) / currentTransform.k;
                    let zoomCenterY = (canvas.height / 2 - currentTransform.y) / currentTransform.k;
                    let pointsToCheck = (this.newSelectedPoints.length > 0) ? this.newSelectedPoints : data2;
                    // 遍历点数据，找到点击的点
                    for (let d of pointsToCheck) {
                        let grid = Math.max(1, Math.floor(1024 / 16));
                        // let x = (grid + 3.5) * parseFloat(d["x"]) + 530;
                        // let y = (grid - 3) * (-parseFloat(d["y"])) + 510;
                        // let x = (grid+5)*(parseFloat(d["x"]))+530;
                        // let y = (grid+31)*(-parseFloat(d["y"]))+480;
                        let x = (grid+10)*(parseFloat(d["x"]))+402;
                        let y = (grid+5.78)*(-parseFloat(d["y"]))+490;

                        // let x = (grid-2)*(parseFloat(d["x"]))+560;
                        // let y = (grid-3.5)*(-parseFloat(d["y"]))+435;


                        let dx1 = x - zoomCenterX;
                        let dy1 = y - zoomCenterY;

                        x = canvasCenterX + dx1 * currentTransform.k;
                        y = canvasCenterY + dy1 * currentTransform.k;

                        let dx = x - mouseX;
                        let dy = y - mouseY;
                        let distance = Math.sqrt(dx * dx + dy * dy);

                        if (distance < hoverRadius) { // 点击的点
                            clickedPoint = d;
                            break;
                        }
                    }
                    // 清空之前的内容
                    document.getElementById("promptDisplay").innerText = "";
                    document.getElementById("Score").innerText = "";
                    document.getElementById("scoreSimilarity").innerText = "";
                    document.getElementById("defaultCaption").innerText = "";
                    document.getElementById("imageDisplay").src = "";
                    document.getElementById("imageDisplay").style.display = "none";
                    document.getElementById("image-thumbnails").innerHTML = '';
                    console.log("click",clickedPoint)

                    // 如果找到了新的点，显示新内容
                    if (clickedPoint) {
                        let promptText = clickedPoint.prompt;
                        let imagePath = clickedPoint.im_path;
                        let score = clickedPoint.score;
                        let index = clickedPoint.index;
                        // console.log(clickedPoint)
                        await this.searchSimilarImage(index)
                        console.log(promptText)
                        let localImagePath = `http://localhost:8000/${imagePath}`;
                        document.getElementById("Score").innerText = "Human Preference Score v2: ";
                        document.getElementById("defaultCaption").innerText = "Caption:";
                        document.getElementById("scoreSimilarity").innerText = score;
                        document.getElementById("promptDisplay").innerText = promptText;
                        document.getElementById("imageDisplay").src = localImagePath;
                        document.getElementById("imageDisplay").style.display = "block";
                    }
                }
            });
            
            canvas.addEventListener("mousedown", (event)=> {
                isDrawing = true;
                isSelecting = false;
                const rect = canvas.getBoundingClientRect();
                rectStartX = event.clientX - rect.left;
                rectStartY = event.clientY - rect.top;
                rectWidth = 0;
                rectHeight = 0;
            });

            canvas.addEventListener("mousemove", (event) =>{
                const rect = canvas.getBoundingClientRect();
                if (!isDrawing) return;
                isSelecting = true;

                let currentX = event.clientX - rect.left;
                let currentY = event.clientY - rect.top;

                rectWidth = currentX - rectStartX;
                rectHeight = currentY - rectStartY;

                this.drawnRectangles = [{ x: rectStartX, y: rectStartY, width: rectWidth, height: rectHeight }]
                console.log("rect",this.drawnRectangles)

                context.clearRect(0, 0, canvas.width, canvas.height);

                context.strokeStyle = "black";
                context.strokeRect(rectStartX, rectStartY, rectWidth, rectHeight);
            });

            canvas.addEventListener("mouseup", async () => {
                isDrawing = false;
                let points = [];

                // 计算矩形边界
                let minX = Math.min(rectStartX, rectStartX + rectWidth);
                let maxX = Math.max(rectStartX, rectStartX + rectWidth);
                let minY = Math.min(rectStartY, rectStartY + rectHeight);
                let maxY = Math.max(rectStartY, rectStartY + rectHeight);

                let zoomCenterX = (canvas.width / 2 - currentTransform.x) / currentTransform.k;
                let zoomCenterY = (canvas.height / 2 - currentTransform.y) / currentTransform.k;

                for (let d of data2) {
                    let grid = Math.max(1, Math.floor(1024 / 16));
                    // let x = (grid+5)*(parseFloat(d["x"]))+530;
                    // let y = (grid+31)*(-parseFloat(d["y"]))+480;
                    let x = (grid+10)*(parseFloat(d["x"]))+402;
                    let y = (grid+5.78)*(-parseFloat(d["y"]))+490;
                    // let x = (grid-2)*(parseFloat(d["x"]))+560;
                    // let y = (grid-3.5)*(-parseFloat(d["y"]))+435;


                    let dx1 = x - zoomCenterX;
                    let dy1 = y - zoomCenterY;

                    x = canvasCenterX + dx1 * currentTransform.k;
                    y = canvasCenterY + dy1 * currentTransform.k;

                    if (x >= minX && x <= maxX && y >= minY && y <= maxY) {
                        points.push(d);
                    }
                }
                if(selectedPoints == points){
                    return;
                }
                else{
                    selectedPoints = points;
                }
                console.log("Selected Points:", selectedPoints);


                if (selectedPoints.length){
                    await this.fetchWordFrequency(selectedPoints,context,currentTransform);
                }

            });



            let zoom = d3.zoom()
                .scaleExtent([1, 16])  
                .on("zoom", (event) =>{
                    let zoomLevel = event.transform.k;
                    console.log("当前缩放级别:", zoomLevel);
                    currentTransform = event.transform;
                    currentZoomLevel = zoomLevel;
                    // console.log("!!",currentZoomLevel)
                    let scaleThreshold = fibonacciLevels[Math.min(Math.floor(zoomLevel)-1,fibonacciLevels.length-1)];
                    console.log(scaleThreshold)
                    if(scaleThreshold==0){
                        data2 = initPoints;
                    }else{
                        data2 = data1.filter(d => d.scaleLevel <= scaleThreshold);
                    }

                    // console.log(data2.length)


                    let newGridSize;
                    if (zoomLevel < 1.5) {
                        label = 1;
                        newGridSize = 64;
                    } else if (zoomLevel < 2.5) {
                        newGridSize = 256;
                        label = 2;
                    } else if (zoomLevel < 3.5) {
                        newGridSize = 1024;
                        label = 3;
                    } else if (zoomLevel < 4.5) {
                        newGridSize = 1024;
                        label = 4;
                    }else if (zoomLevel < 7) {
                        newGridSize = 1024;
                        label = 5;
                    }else if (zoomLevel <= 13) {
                        newGridSize = 1024;
                        label = 6;
                    }
                    else if (zoomLevel <= 25) {
                        newGridSize = 1024;
                        label = 7;
                    }


                    if (currentGridSize !== newGridSize) {

                        let newSize = 512 / zoomLevel;
                        let newX = -event.transform.x * (newSize / size);
                        let newY = -event.transform.y * (newSize / size);

                        viewX = newX;
                        viewY = newY;
                        viewSize = newSize;
                        currentGridSize = newGridSize;
                        currentZoomLevel = zoomLevel;

                        requestAnimationFrame(() => {
                            drawContours(label,currentGridSize, [viewX, viewX + viewSize], [viewY, viewY + viewSize]);


                        });
                    }
                    if (currentGridSize == 1024) {

                        let newSize = 512 / zoomLevel;
                        let newX = -event.transform.x * (newSize / size);
                        let newY = -event.transform.y * (newSize / size);

                        viewX = newX;
                        viewY = newY;
                        viewSize = newSize;
                        currentGridSize = newGridSize;
                        currentZoomLevel = zoomLevel;

                        requestAnimationFrame(() => {
                            drawContours(label,currentGridSize, [viewX, viewX + viewSize], [viewY, viewY + viewSize]);

                        });
                    }

                    contourGroup.attr("transform", event.transform);
                    this.drawPoints(data2,context,event.transform)

                });

            svg.call(zoom);
            drawContours(label,currentGridSize, [0, 1], [0, 1]);
            this.drawPoints(data2,context,defaultTransform);

        },

        async searchSimilarImage(imagePath){
            try {
                const response = await axios.post("http://127.0.0.1:5000/api/test/similar-search/", {
                    index: imagePath
                });
                let imagePaths = response.data.slice(1); 
                console.log(imagePaths)
                const thumbnailsContainer = document.getElementById("image-thumbnails");

                imagePaths.forEach(path => {
                    const img = document.createElement("img");
                    img.src = `http://localhost:8000/${path}`;
                    img.style.width = "85px";
                    img.style.height = "85px";
                    img.style.objectFit = "cover";
                    img.style.borderRadius ="5px";
                    thumbnailsContainer.appendChild(img);
                });
                // this.drawHistogram();
            } catch (error) {
                console.error("Error:", error);
            }

        },

        async fetchWordFrequency(selectedPoints,context,transform) {
            const prompts = selectedPoints.map(d => d.prompt);
            const im_path = selectedPoints.map(d => d.im_path);
            const index = selectedPoints.map(d => d.index);
            console.log(index);

            try {
                const response = await axios.post("http://127.0.0.1:5000/api/test/analyze-prompts/", {
                    prompts: prompts,
                    paths: im_path,
                    index:index
                });

                let result = response.data; 
                console.log(result)
                echarts.registerTransform(ecStat.transform.histogram); 
                this.drawHistogram(selectedPoints, result,context,transform)
                // console.log(this.wordFrequency);
                // await this.calculateConcept(selectedPoints);
                // this.drawHistogram();
            } catch (error) {
                console.error("Error:", error);
            }
        },

        drawHistogram(selectedPoints, clusterSim,context,transform){      
            echarts.registerTransform(ecStat.transform.histogram);   
            console.log("select",selectedPoints)
            const chartContainer = document.getElementById("graph-container"); 
            chartContainer.innerHTML = '';
            for (const keyword in clusterSim) {
                const similarities = clusterSim[keyword];
                var binCount = 5;  // 设定固定的 bin 数量
                var minVal = Math.min(...similarities);
                var maxVal = Math.max(...similarities);
                var interval = (maxVal - minVal) / binCount;

                // 初始化 bins
                var bins = new Array(binCount).fill(0);
                let binMapping = new Array(binCount).fill().map(() => []);

                // 手动分桶
                similarities.forEach((value,idx) => {
                    let index = Math.floor((value - minVal) / interval);
                    if (index >= binCount) index = binCount - 1; // 确保不会超出范围
                    bins[index]++;
                    binMapping[index].push(idx); 
                });

                    // 生成 ECharts 所需格式
                var data = bins.map((count, i) => {
                    return [minVal + i * interval, minVal + (i + 1) * interval, count];
                });
                    
                const chartWrapper = document.createElement('div');
                chartWrapper.classList.add('chart-wrapper');
                chartContainer.appendChild(chartWrapper);
               
                const myChart = echarts.init(chartWrapper);

                    // 自定义渲染效果
                function renderItem(params, api) {
                        // 这个根据自己的需求适当调节
                    var yValue = api.value(2);
                    var start = api.coord([api.value(0), yValue]);
                    var size = api.size([api.value(1) - api.value(0), yValue]);
                    var style = api.style();

                    return {
                            // 矩形及配置
                        type: 'rect',
                        shape: {
                            x: start[0] + 1,
                            y: start[1],
                            width: size[0] - 2,
                            height: size[1]
                        },
                        style: style
                    };
                }

                const option = {
                    title: {
                        text: `${keyword.replace(/(.{30})/g, '$1\n')}`,
                        left: 'center',
                        top: 20,
                        textStyle: {
                            fontSize: 12,
                            width:130,
                            overflow:'break'
                        },
                    },
                    color: '#6a636f',
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    xAxis: {
                        name: 'Similarity',
                        type: 'value',                           
                        min: 0,
                        max: 1,
                            
                    },
                    yAxis: {
                        type: 'value',                            
                        axisLabel: {
                            formatter: '{value}'  // 格式化标签显示
                        }
                    },
                    series: [{
                        name: 'Similarity',
                        type: 'custom',  // 使用 bar 类型绘制直方图
                        renderItem: renderItem,
                        encode: {
                            // 表示将data中的data[0]和data[1]映射到x轴
                        x: [0, 1],
                            // 表示将data中的data[2]映射到y轴
                        y: 2,
                            // 表示将data中的data[2]映射到tooltip
                        tooltip: 2,
                            // 表示将data中的data[2]映射到label
                        label: 2
                    },
                    data: data                            
                    }],
                    grid: {
                        left: '4%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                        
                };

                // 使用刚指定的配置项和数据显示图表
                myChart.setOption(option);
                myChart.on('click', async (params) =>{
                    console.log('Click event triggered', params); 

                    let binIndex = params.dataIndex;
                    console.log(binIndex)

                    // 获取该 bin 内的索引列表
                    let selectedIndices = binMapping[binIndex] || [];
                    console.log(selectedIndices)

                    if (selectedIndices.length > 0) {
                        this.newSelectedPoints = selectedIndices.map(i => selectedPoints[i]);
                        console.log("new",this.newSelectedPoints)
                        this.drawPoints(this.newSelectedPoints,context,transform);
                        // console.log("found3")

                    }
                });


            }

        },


    },


}
</script>
<style>
.maiden-orange-regular {
  font-family: "Maiden Orange", serif;
  font-weight: 400;
  font-style: normal;
  font-size: 133px;
  color: #65513C;
}

.chart-wrapper {
    width: 30%; 
    height: 150px;
    position: relative;
    /* max-width: 100px; 
    min-width: 250px;  */
}
.chart-wrapper canvas {
    width: 100%;  /* 让canvas宽度填满容器 */
    height: 100%; /* 让canvas高度填满容器 */
}
#main-image-container::-webkit-scrollbar {
    display: none;
}

circle {
    pointer-events: all;
}

.axis {
    stroke: #000;
    stroke-width: 1.5px;
}

.node circle {
    stroke: #000;
}

.link {
    /* fill: none; */
    fill: blue;
    stroke: #999;
    stroke-width: 1.5px;
    stroke-opacity: .3;
}

/* .path {
    fill: blue
} */
.link.active {
    stroke: red;
    stroke-width: 2px;
    stroke-opacity: 1;
}

.node circle.active {
    stroke: red;
    stroke-width: 3px;
}

.tooltip {
    z-index: 1;
    width: 300px;
    height: 300px;
    border: 1px solid;
    position: absolute;
    /* position:relative; */
    visibility: hidden;
    background-color: white;
}

.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.avatar-uploader .el-upload:hover {
    border-color: #409EFF;
}

.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
}

.avatar {
    width: 178px;
    height: 178px;
    display: block;
}


.contour {
    mix-blend-mode: multiply;
}

.header {
    text-align: center;
    position: relative;
    /* padding: 20px 0; */
    padding: 2px 0;
}

.header::before,
.header::after {
    content: "";
    position: absolute;
    top: 50%;
    /* top: 20%; */
    width: 25%;
    border-top: 2.3px solid #65513C;
}

.header::before {
    left: 0;
}

.header::after {
    right: 0;
}

.header2 {
    text-align: center;
    position: relative;
    /* padding: 20px 0; */
    padding: 2px 0;
}

.header2::before,
.header2::after {
    content: "";
    position: absolute;
    top: 50%;
    /* top: 20%; */
    width: 35%;
    border-top: 2.3px solid #65513C;
}

.header2::before {
    left: 0;
}

.header2::after {
    right: 0;
}

html {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

*::-webkit-scrollbar {
    width: 10px;
}

*::-webkit-scrollbar-thumb {
    background: #ccc;
    border-radius: 5px;
}

* {
    scrollbar-width: 10px;
    scrollbar-base-color: green;
    scrollbar-track-color: red;
    scrollbar-arrow-color: blue;
}

.text-element {
    cursor: default;
    /* or any cursor value you prefer, e.g., auto, inherit, etc. */
}

/*Chrome*/
@media screen and (-webkit-min-device-pixel-ratio:0) {
    input[type='range'] {
        overflow: hidden;
        width: 150px;
        -webkit-appearance: none;
        /* background-color: #9a905d; */
        background-color: rgb(230, 230, 230);

    }

    input[type='range']::-webkit-slider-runnable-track {
        height: 10px;
        -webkit-appearance: none;
        color: #919191;
        margin-top: -1px;
    }

    input[type='range']::-webkit-slider-thumb {
        width: 10px;
        -webkit-appearance: none;
        height: 10px;
        cursor: ew-resize;
        background: #434343;
        box-shadow: -80px 0 0 80px #919191;
    }

}


.custom-button {
    background-color: "yellow";
    border-color: "yellow";
    color: "white";
}

/* Define hover and active states */
.custom-button:hover {
    background-color: "yellow";
    border-color: "yellow"
}

.custom-button:active {
    background-color: "yellow";
    border-color: "yellow"
}

.rectangle {
    box-sizing: border-box;
    position: relative; /* 使其成为子元素的参考点 */
    width: 280px;
    height: 40px;
    background: #FFFFFF;
    border: 2.5px solid rgba(44, 62, 80, 0.6);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 10px;

}

.rectangle span {
  font-size: 20px;

}
.dropdown {
    position: absolute;
    top: 0%;
    background: white;
    border: 2.5px solid rgba(44, 62, 80, 0.6);
    border-radius: 10px;
    padding: 10px;
    width: 280px;
    z-index: 8;
    margin-left: 40px;
}

.svg-button {
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
    position: absolute;
    margin-left: 240px;
    align-items: center;
    z-index: 10;

}
.dropdown-item {
  cursor: pointer;
  font-size: 20px; 
  padding: 10px 0;
}

.dropdown-item:hover {
  background-color: #f8ecdd; 
  border-radius: 10px;
}

.buttons {
  display: flex;
  flex-wrap: wrap; /* 允许按钮换行 */
  gap: 10px; /* 按钮之间的间距 */

  margin-left: 30px;
  margin-top: 20px;
  z-index: 10;
}

.rectangle-button {
  background-color: #A3978A;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 15px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
}

.rectangle-button:hover {
  background-color: #65513C;
}

.rectangle-button.active {
  background-color: #65513C;
}

#datasetdetails strong {
  font-weight: bold;
  font-size: 20px;
  color: #2C3E50;
}
#datasetdetails p {
  margin: 10px 0; 
  font-size: 18px;
}


</style>

