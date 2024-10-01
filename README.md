# Brain MRI Metastasis Segmentation

![image](https://github.com/user-attachments/assets/c0079d81-1782-4d22-95bc-dcf71e69e450)

## Objective
This project implements and compares two architectures, **Nested U-Net (U-Net++)** and **Attention U-Net**, for brain MRI metastasis segmentation. The project involves preprocessing MRI images, training and evaluating both models using the DICE score, and developing a web application using **FAST API** and **Streamlit** to showcase the segmentation results.

## Dataset
The dataset consists of Brain MRI images and corresponding metastasis segmentation masks.

- Dataset Link: [Download Dataset](https://dicom5c.blob.core.windows.net/public/Data.zip)
- **Note**: Ignore images that are missing corresponding masks.
- **Dataset Structure**:
  - `train/`: Training images and masks
  - `test/`: Testing images and masks

Split the dataset into 80% training and 20% testing sets.

## Assignment Details

### 1. Data Preprocessing
- Implement **CLAHE** (Contrast Limited Adaptive Histogram Equalization) preprocessing to enhance metastasis visibility in MRI images.
- Ensure proper **normalization** and **augmentation** (e.g., rotations, flips) for robust model training.

### 2. Model Implementation
- Implement the following architectures for metastasis segmentation:
  - **Nested U-Net (U-Net++)**
  - **Attention U-Net**

### 3. Model Training and Evaluation
- Train both models on the preprocessed dataset.
- Use **DICE Score** as the primary evaluation metric for segmentation accuracy.
- Compare the performance of both models based on the DICE Score and qualitative results.

### 4. Web Application Development
- Create a **FAST API** backend to serve the best performing metastasis segmentation model.
- Develop a **Streamlit** UI that allows users to upload brain MRI images and view metastasis segmentation results in real-time.

### 5. Documentation
The project includes the following documentation:
- Explanation of **Nested U-Net** and **Attention U-Net** architectures.
- Instructions on setting up the project.
- Challenges specific to brain metastasis segmentation and how they were addressed.
- Future improvements and potential clinical applications.

## Project Setup

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/metastasis-segmentation.git
   cd metastasis-segmentation

### Key Sections
- **Objective**: Explains the purpose of the project.
- **Dataset**: Provides the dataset link and instructions for use.
- **Assignment Details**: Covers preprocessing, model implementation, training, and evaluation.
- **Project Setup**: Includes instructions to clone the repo, install dependencies, and run the backend/frontend.
- **Model Architectures**: Brief explanations of the architectures.
- **Evaluation Metric**: DICE Score formula and use.
- **Results**: Compares the models' DICE scores.
- **Challenges and Future Work**: Highlights obstacles and potential improvements.

This template can be used directly in your project’s `README.md` file. Let me know if you need further customization!
