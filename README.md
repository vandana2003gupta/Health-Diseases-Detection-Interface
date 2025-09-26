#  Health Diseases Detection Interface

## Live Application - https://health-disease-detection-interface.streamlit.app/
(note) Plz view in light theme

## Project Overview
This is a **Health Disease Detection Interface** built using **Streamlit** which enables users to predict multiple diseases based on medical parameters. It includes an intuitive web interface for ease of use.

Currently, it offers detection for:
- **Diabetes**
- **Heart Disease**
- **Parkinson’s Disease**
- **Autism**
- **Yoga Posture Correction** *(via external link)*

It also provides:
- **Yoga Posture Corrector (External Tool)**
- **AI-powered Medical Report Analysis Bot** (using Gemini-1.5-Flash)
- **Feedback Collection**

## Live Demo
You can access the deployed app here:  
👉 [Health Disease Detection Interface (Streamlit Cloud)](https://health-disease-detection-interface.streamlit.app/)

## Features
- Easy-to-use web interface for disease prediction.
- Multiple disease detection in a single app.
- Sidebar navigation for disease selection.
- Custom theme and responsive layout.
- Report and Medical Image Analysis Bot via Gen Ai
- Integrated external link for Yoga Posture Correction.

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Welcome Page**            | Overview of app features and intro image                                    |
| **Autism Detection**        | Placeholder (under development)                                             |
| **Diabetes Detection**      | Predicts diabetes using Random Forest-based ML model                        |
| **Heart Disease Detection** | Predicts heart disease with Logistic Regression/Random Forest model         |
| **Parkinson’s Detection**   | Detects Parkinson’s Disease using SVC model                                 |
| **Yoga Posture Corrector**  | Redirects users to an external posture correction tool                      |
| **Report Analysis Bot**     | AI-powered bot that analyzes medical images and PDFs using Generative Ai    |
| **Feedback Section**        | Collects user ratings and feedback                                          |


## Technologies Used

| Technology                  | Purpose                                   |
|-----------------------------|-------------------------------------------|
| **Python**                  | Core programming language                 |
| **Streamlit**               | Web App framework                         |
| **scikit-learn**            | Machine Learning models                   |
| **Pandas**                  | Data manipulation                         |
| **NumPy**                   | Numerical operations                      |
| **Pickle**                  | Model Serialization/Deserialization       |
| **Google Generative AI**    | Gemini-1.5-flash for image/text analysis  |
| **PIL (Pillow)**            | Image Processing                          |
| **PyMuPDF (fitz)**          | PDF Text Extraction                       |
| **Streamlit Option Menu**   | Sidebar navigation menu                   |
| **Custom CSS & Images**     | Styling and UI Enhancements               |


## Models Used

| Disease                     | Model Type           | Algorithm Used                     |
|-----------------------------|----------------------|------------------------------------|
| **Diabetes Prediction**     | Classification Model | Random Forest Classifier           |
| **Heart Disease Prediction**| Classification Model | Logistic Regression / Random Forest|
| **Parkinson’s Detection**   | Classification Model | Support Vector Classifier (SVC)    |
| **Autism Detection**        | - (Under Development)| -                                  |



## Local Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/vandana2003gupta/Health-Diseases-Detection-Interface.git
cd Health-Diseases-Detection-Interface
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

## Demo photographs

<img width="1917" height="1027" alt="image" src="https://github.com/user-attachments/assets/e0260ecd-00af-45a4-bf9e-5c428d3c337d" />
<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/11f12537-23ed-4c32-a5a8-b68fceeed89e" />
<img width="1919" height="1037" alt="image" src="https://github.com/user-attachments/assets/ba3c9763-c894-4b39-b560-c44c0df96a89" />
<img width="1919" height="1028" alt="image" src="https://github.com/user-attachments/assets/898362e6-69c9-47a1-a10a-33b373434289" />
<img width="1919" height="1032" alt="image" src="https://github.com/user-attachments/assets/0e356745-63f2-4e91-a38c-aa96dbe91cfc" />
<img width="1919" height="1032" alt="image" src="https://github.com/user-attachments/assets/2b792070-46b0-43ff-bb3c-93dd0a486816" />
<img width="1919" height="984" alt="image" src="https://github.com/user-attachments/assets/e2aa0c4a-a7d3-4979-9d44-bb6194244139" />
<img width="1919" height="985" alt="image" src="https://github.com/user-attachments/assets/7b5f5ed1-0943-459b-9e60-47d654efbce5" />
<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/5beb0078-be87-4a1e-a34d-d2a7f6c15905" />
<img width="1919" height="987" alt="image" src="https://github.com/user-attachments/assets/a8bade1f-3380-4733-ae0f-cea95bfd8183" />











