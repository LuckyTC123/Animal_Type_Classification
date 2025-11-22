# Animal_Type_Classification
developing the ML model which can extract the keypoints from the cow image and determining the health using morphological character of cow
# 🐄 Deep Learning for Cow Morphological Analysis & Breeding Suitability

## 📌 Project Overview
This project is my final year work focused on applying **Deep Learning** to livestock analysis.  
The goal is to evaluate cow morphology (length, width, and other body parameters) from images and determine **breeding suitability based on weather conditions**.

Key steps:
- Annotated **100 cow images** in **COCO format**.
- Fine-tuned **Detectron2** for **keypoint detection**.
- Extracted morphological characteristics (length, width, ratios).
- Computed body parameters to assess **breeding suitability**.

---

## 🚀 Features
- 🖼️ **Image-based analysis**: Input cow images, output keypoints & body measurements.
- 🔑 **Keypoint detection**: Detectron2 model fine-tuned on custom dataset.
- 📏 **Morphological evaluation**: Length, width, and derived parameters.
- 🌦️ **Breeding suitability**: Decision-making based on morphological parameters and weather suitability.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **PyTorch**
- **Detectron2**
- **OpenCV**
- **COCO Dataset Format**

---

## 📂 Dataset
- 100 annotated cow images in **COCO format**.
- Custom annotations include keypoints for morphological analysis.

---
## 🔮 Future Usage
This project lays the foundation for advanced applications in livestock management and breeding programs. Potential future directions include:

- 📈 **Scaling dataset**: Expanding beyond 100 images to thousands for improved accuracy and generalization.
- 🎥 **Real-time monitoring**: Integrating video streams for continuous livestock tracking.
- 🌍 **IoT integration**: Combining sensor data (temperature, humidity, feed intake) with morphological analysis.
- 🧠 **Advanced models**: Exploring transformer-based architectures for more robust keypoint detection.
- 🐮 **Cross-species adaptation**: Extending methodology to other livestock such as buffalo, goats, or sheep.
- 📊 **Decision support systems**: Building dashboards for farmers to visualize breeding suitability and health metrics.

---

## 📜 License
This repository is licensed under the **MIT License**.  

You are free to:
- ✅ Use the code for personal, academic, or commercial projects.
- ✅ Modify and distribute with proper attribution.

Limitations:
- ❌ No warranty is provided — use at your own risk.
- ❌ The author is not liable for any misuse or damages arising from this project.

For full details, see the [MIT License](https://opensource.org/licenses/MIT).


## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/cow-breeding-analysis.git
cd cow-breeding-analysis
pip install -r requirements.txt
