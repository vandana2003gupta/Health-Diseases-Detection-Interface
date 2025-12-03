import os
import pickle
import base64
import io
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="Health Care Analyzer", layout="wide")

def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
    <style>
    .stTextInput > div > div > input, 
    .stSelectbox > div > div>div,
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        border: 1px solid #FFA07A;
        border-radius: 10px;
        padding: 0.4rem;
    }
    .stButton button {
        border-radius: 10px;
        background-color: #ff944d;
        color: white;
    }
    .stButton button:hover {
        background-color: #ff6600;
    }
    h1 {
        text-align: center;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

try:
    with open('Diseases/Heart-Disease-Prediction/heart.pkl', 'rb') as file:
        heart_model = pickle.load(file)
    with open('Diseases/Diabetes-Prediction/diabetes.pkl', 'rb') as file:
        diabetes_model = pickle.load(file)
    with open('Diseases/Parkinson-Disease-Prediction/Parkinsons.pkl', 'rb') as file:
        parkinsons_model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.stop()


with st.sidebar:
    selected = option_menu('Services',
        ['Welcome', 'Autism Prediction', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction',
         'Yoga Posture Corrector', 'Report Analysis Bot', 'Feedback'],
        default_index=0
    )


if selected == 'Welcome':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Health Disease Prediction Interface</h1>", unsafe_allow_html=True)
    st.write("This application detects diseases like Diabetes, Heart, and Parkinson's using ML, and includes medical report, rash analysis bot & yoga assistance.")
    st.image("Img1.webp", use_container_width=True)


elif selected == 'Autism Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Autism Prediction</h1>", unsafe_allow_html=True)
    st.write("Note - Autism section is under development.")
    st.image("Img2.jpg", use_container_width=True)


elif selected == 'Diabetes Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Diabetes Detection using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: pregnancies = st.text_input('Number of Pregnancies', '0')
    with col2: glucose = st.text_input('Glucose Level', '120')
    with col3: blood_pressure = st.text_input('Blood Pressure', '70')
    with col1: skin_thickness = st.text_input('Skin Thickness', '20')
    with col2: insulin = st.text_input('Insulin Level', '80')
    with col3: bmi = st.text_input('BMI', '25')
    with col1: diabetes_pedigree = st.text_input('Diabetes Pedigree Function', '0.5')
    with col2: age = st.text_input('Age', '30')

    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(pregnancies), float(glucose), float(blood_pressure),
                          float(skin_thickness), float(insulin), float(bmi),
                          float(diabetes_pedigree), float(age)]
            result = diabetes_model.predict([input_data])[0]
            st.success("The person is not diabetic." if result == 1 else "The person is diabetic.")
        except Exception as e:
            st.error(f"Error: {str(e)}. Please enter valid numbers")
    st.image("Diseases/Diabetes-Prediction/img3.jpg", use_container_width=True)


elif selected == 'Heart Disease Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age', '50')
    with col2: sex = st.selectbox('Sex', ['Male', 'Female'])
    with col3: cp = st.selectbox('Chest Pain Type', ['0: Typical', '1: Atypical', '2: Non-anginal', '3: Asymptomatic'])
    with col1: trestbps = st.text_input('Resting BP', '120')
    with col2: chol = st.text_input('Cholesterol', '200')
    with col3: fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
    with col1: restecg = st.selectbox('Resting ECG', ['0: Normal', '1: ST-T Abnormality', '2: LV Hypertrophy'])
    with col2: thalach = st.text_input('Max Heart Rate', '150')
    with col3: exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])
    with col1: oldpeak = st.text_input('ST Depression', '0.0')
    with col2: slope = st.selectbox('Slope', ['0: Upsloping', '1: Flat', '2: Downsloping'])
    with col3: ca = st.text_input('Major Vessels Colored', '0')
    with col1: thal = st.selectbox('Thalassemia', ['0: Normal', '1: Fixed Defect', '2: Reversable Defect'])

    if st.button('Heart Disease Test Result'):
        try:
            sex = 1 if sex == 'Male' else 0
            cp = int(cp.split(":")[0])
            fbs = int(fbs.split(":")[0])
            restecg = int(restecg.split(":")[0])
            exang = int(exang.split(":")[0])
            slope = int(slope.split(":")[0])
            thal = int(thal.split(":")[0])
            input_data = [
                float(age), sex, cp, float(trestbps), float(chol), fbs,
                restecg, float(thalach), exang, float(oldpeak),
                slope, float(ca), thal
            ]
            result = heart_model.predict([input_data])[0]
            st.success("The person has heart disease." if result == 0 else "The person does not have heart disease.")
        except Exception as e:
            st.error(f"Input Error: {str(e)}")
    st.image("Diseases/Heart-Disease-Prediction/img4.png", use_container_width=True)


elif selected == 'Parkinsons Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    inputs = [st.text_input(label, default) for label, default in zip(
        ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
         "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
         "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
         "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"],
        ['120', '140', '100', '0.005', '0.00005', '0.003', '0.004', '0.009', '0.03', '0.3',
         '0.01', '0.02', '0.02', '0.01', '0.02', '20', '0.4', '0.7', '-6.5', '0.1', '2.3', '0.2']
    )]

    if st.button("Parkinson's Test Result"):
        try:
            result = parkinsons_model.predict([list(map(float, inputs))])[0]
            st.error("Parkinson's Disease predicted." if result == 1 else "No Parkinson's Disease.")
        except Exception as e:
            st.error(f"Input Error: {str(e)}")
    st.image("Diseases/Parkinson-Disease-Prediction/img.webp", use_container_width=True)
    
 

elif selected == 'Yoga Posture Corrector':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>🧘‍♂️ Yoga Posture Corrector</h1>", unsafe_allow_html=True)
    if st.button("Open Urban Yogi Pose Corrector"):
        st.components.v1.iframe("https://urban-yogi-main.vercel.app", height=800, scrolling=True)
    st.image("Urban-Yogi-Main/img6.png", use_container_width=True)


elif selected == 'Report Analysis Bot':
    import google.generativeai as genai
    from PIL import Image
    import io
    import fitz  # PyMuPDF

    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>📄 Medical Report & Image Chatbot</h1>", unsafe_allow_html=True)

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    if 'gemini_image_bytes' not in st.session_state:
        st.session_state.gemini_image_bytes = None
    if 'gemini_pdf_text' not in st.session_state:
        st.session_state.gemini_pdf_text = ""
    if 'gemini_history' not in st.session_state:
        st.session_state.gemini_history = []

    # File uploader (image or PDF)
    uploaded_file = st.file_uploader("📤 Upload a medical image or report (PDF)", type=["jpg", "jpeg", "png", "pdf"])

    if uploaded_file:
        file_type = uploaded_file.type

        # image upload 
        if "image" in file_type:
            st.image(uploaded_file, caption="📍 Uploaded Medical Image", use_column_width=True)
            image = Image.open(uploaded_file).convert("RGB")
            image_bytes_io = io.BytesIO()
            image.save(image_bytes_io, format="JPEG")
            st.session_state.gemini_image_bytes = image_bytes_io.getvalue()

        # PDF upload
        elif file_type == "application/pdf":
            st.markdown("PDF uploaded. Extracting text...")
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            pdf_text = ""
            for page in doc:
                pdf_text += page.get_text()
            doc.close()
            st.session_state.gemini_pdf_text = pdf_text
            st.text_area(" Extracted PDF Text", pdf_text, height=200)

    # Question input
    question = st.text_input("Ask a question about the uploaded image or PDF")

    if st.button("🔍 Ask Gemini") and question:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")

            content_parts = []
            if st.session_state.gemini_image_bytes:
                content_parts.append({"inline_data": {"mime_type": "image/jpeg", "data": st.session_state.gemini_image_bytes}})
            if st.session_state.gemini_pdf_text:
                content_parts.append({"text": st.session_state.gemini_pdf_text})

            content_parts.append({"text": question})

            with st.spinner("Bot is thinking..."):
                response = model.generate_content(content_parts)
                reply = response.text

            # Save chat history
            st.session_state.gemini_history.append({
                "question": question,
                "response": reply
            })

            st.success("Gemini's Response:")
            st.markdown(reply)

        except Exception as e:
            st.error(f"Gemini Error: {str(e)}")

    if st.session_state.gemini_history:
        st.markdown("---")
        st.subheader("Chat History")
        for chat in reversed(st.session_state.gemini_history):
            st.markdown(f"""
            <div style='background-color:#f3f3f3;padding:10px;border-radius:8px;margin-bottom:10px'>
            <b> You:</b> {chat['question']}<br><br>
            <b> Bot:</b> {chat['response']}
            </div>
            """, unsafe_allow_html=True)


elif selected == 'Feedback':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1> Feedback Section</h1>", unsafe_allow_html=True)
    feedback = st.text_area("Write your suggestions below:")
    rating = st.slider("How was your experience?", 0, 10, 5)
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
