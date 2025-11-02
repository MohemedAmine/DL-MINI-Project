# DL-MINI-Project
# 🧠 Brain MRI Denoising with Deep Convolutional Autoencoders

This project applies deep learning techniques to improve the quality of noisy brain MRI scans using convolutional autoencoders. The goal is to assist diagnosis by enhancing image clarity while preserving important medical details like tumor contours.

## 📌 Table of Contents
- [Project Description](#project-description)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Gradio App](#gradio-app)
- [Future Work](#future-work)
- [References](#references)

## 📖 Project Description
Brain MRI images are often affected by noise during acquisition, which can hinder diagnosis. We propose a deep learning-based solution using **convolutional autoencoders** to denoise these images. Our system:
- Removes Gaussian noise from brain MRI scans.
- Maintains critical visual information for clinical use.
- Can be integrated into diagnostic pipelines.

## 🧠 Dataset
We used a publicly available dataset from Kaggle that contains:
- MRI images with and without brain tumors.
- Images were resized to 64x64 and normalized.
- Gaussian noise was artificially added for training.

Dataset link: [Kaggle Brain MRI Images](https://www.kaggle.com/datasets/)

## 🏗️ Model Architecture
We designed and trained two convolutional autoencoders:

### Autoencoder 1 (Baseline)
- Simple encoder-decoder with two convolution and pooling layers each.

### Autoencoder 2 (Improved)
- Deeper architecture with more filters and better reconstruction quality.

Loss Function: Mean Squared Error (MSE)  
Optimizer: Adam

## 📊 Results

| Model           | MSE ↓   | PSNR ↑     |
|----------------|---------|------------|
| Autoencoder 1  | 0.0106  | ~18.8 dB   |
| Autoencoder 2  | 0.0087  | ~19.9 dB   |

Qualitative results show sharper, cleaner reconstructions with improved tumor visibility.

## ⚙️ Installation
```bash
git clone https://github.com/MohemedAmine/brain-mri-autoencoder.git
cd brain_tumor_denoising
pip install -r requirements.txt
```

---

## 👨‍💻 Author
**Mohamed amine OULAD SAID**  
> AIDS Student

 
📧 Contact: *mohamedamineouledsaid10@gmail.com*  

---

## 🧾 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
