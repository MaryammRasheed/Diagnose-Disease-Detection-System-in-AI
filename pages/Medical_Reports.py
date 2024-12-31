import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# App title
st.title("🩺 Medical Report Generator")
st.markdown("Predict diseases based on symptoms and generate a medical report.")

# Generate mock datasets dynamically
def create_mock_data():
    symptoms = ["Fever", "Cough", "Headache", "Nausea", "Fatigue", "Body Pain"]
    
    # Disease data (this will align with symptoms)
    diseases = ["Flu", "Cold", "Migraine", "Food Poisoning", "Dengue"]
    
    # Disease descriptions
    descriptions = [
        "A viral infection causing fever, chills, and body aches.",
        "A respiratory infection causing coughing and congestion.",
        "Severe headaches often accompanied by nausea.",
        "Illness caused by consuming contaminated food.",
        "A mosquito-borne viral infection causing high fever and rash."
    ]
    
    # Disease precautions
    precautions = {
        "Flu": ["Drink warm fluids", "Rest well", "Take paracetamol"],
        "Cold": ["Use nasal sprays", "Drink ginger tea", "Avoid cold drinks"],
        "Migraine": ["Avoid bright lights", "Take pain relievers", "Stay hydrated"],
        "Food Poisoning": ["Avoid eating outside", "Stay hydrated", "Take prescribed antibiotics"],
        "Dengue": ["Use mosquito repellents", "Wear full-sleeve clothes", "Consult a doctor"]
    }
    
    # Disease medicines
    medicines = {
        "Flu": ["Paracetamol", "Ibuprofen", "Vitamin C"],
        "Cold": ["Cough syrup", "Steam inhalation", "Antihistamines"],
        "Migraine": ["Painkillers", "Caffeine tablets", "Naproxen"],
        "Food Poisoning": ["Activated charcoal", "ORS solution", "Antibiotics"],
        "Dengue": ["Paracetamol", "IV fluids", "Anti-viral drugs"]
    }

    # Create DataFrame where each symptom corresponds to a disease
    data = {
        "Symptoms": symptoms * len(diseases),  # Repeat symptoms for each disease
        "Diseases": diseases * len(symptoms),  # Repeat diseases for each symptom
        "Descriptions": [desc for desc in descriptions for _ in symptoms],  # Repeat descriptions
        "Precautions": [precautions[disease] for disease in diseases for _ in symptoms],
        "Medicines": [medicines[disease] for disease in diseases for _ in symptoms]
    }
    
    # Create and return DataFrame
    return pd.DataFrame(data)

# Create mock data
mock_data = create_mock_data()

# Sidebar for selecting symptoms
st.sidebar.header("Select Symptoms")
symptoms = mock_data["Symptoms"].unique()  # Get unique symptoms
selected_symptoms = st.sidebar.multiselect("Select your symptoms:", symptoms)

# Create a simple dataset for RandomForest training
if selected_symptoms:
    # Generate training data
    num_samples = 100
    np.random.seed(42)
    X = np.random.choice([0, 1], size=(num_samples, len(symptoms)))
    y = np.random.choice(mock_data["Diseases"].unique(), size=num_samples)
    disease_mapping = {disease: i for i, disease in enumerate(mock_data["Diseases"].unique())}
    y_encoded = np.array([disease_mapping[disease] for disease in y])
    
    # Train RandomForest Model
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Create user input for prediction
    input_data = np.zeros(len(symptoms))
    for symptom in selected_symptoms:
        input_data[symptoms.tolist().index(symptom)] = 1
    input_data = input_data.reshape(1, -1)
    
    # Predict the disease
    prediction = model.predict(input_data)[0]
    predicted_disease = [d for d, i in disease_mapping.items() if i == prediction][0]
    
    # Display prediction results
    st.subheader("Predicted Disease")
    st.success(f"The detected disease is: **{predicted_disease}**")
    
    # Display disease description
    disease_info = mock_data[mock_data["Diseases"] == predicted_disease].iloc[0]
    st.subheader("Disease Description")
    st.write(disease_info["Descriptions"])
    
    # Display precautions
    st.subheader("Precautions")
    for precaution in disease_info["Precautions"]:
        st.write(f"- {precaution}")
    
    # Display medicines
    st.subheader("Recommended Medicines")
    for medicine in disease_info["Medicines"]:
        st.write(f"- {medicine}")
    
    # Generate and download the medical report
    report = f"""
    Medical Report
    
    Predicted Disease: {predicted_disease}
    Description: {disease_info['Descriptions']}
    Precautions: {', '.join(disease_info['Precautions'])}
    Recommended Medicines: {', '.join(disease_info['Medicines'])}
    """
    st.download_button(label="Download Report", data=report, file_name="medical_report.txt", mime="text/plain")
