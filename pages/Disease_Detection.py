import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import plotly.graph_objs as go

# Define symptoms list (50 symptoms)
symptoms = [
    "Fever", "Cough", "Headache", "Fatigue", "Shortness of breath", 
    "Sore throat", "Body ache", "Nausea", "Vomiting", "Diarrhea", 
    "Loss of appetite", "Dizziness", "Chest pain", "Rash", "Chills",
    "Joint pain", "Runny nose", "Congestion", "Sweating", "Abdominal pain",
    "Muscle weakness", "Night sweats", "Loss of taste", "Loss of smell", 
    "Coughing up blood", "Difficulty breathing", "Difficulty swallowing", 
    "Mouth ulcers", "Swollen lymph nodes", "Skin discoloration", "Cough with mucus", 
    "Hoarseness", "Weight loss", "Frequent urination", "Swelling in feet", 
    "Tremors", "Numbness", "Memory loss", "Confusion", "Severe headache", 
    "Eye pain", "Dry eyes", "Blurred vision", "Painful urination", "Blood in urine",
    "Dark urine", "Persistent pain", "Heavy menstrual bleeding", "Abnormal sweating", 
    "Cold hands and feet", "Insomnia", "Frequent infections"
]

# Generating random dataset (Replace this with your real data if needed)
np.random.seed(42)
X = np.random.randint(0, 2, size=(1000, len(symptoms)))  # 1000 samples, 50 symptoms
y = np.random.choice(["Flu", "Cold", "COVID-19", "Malaria", "Pneumonia"], size=1000)

# Create DataFrame
df = pd.DataFrame(X, columns=symptoms)
df['Disease'] = y

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[symptoms], df['Disease'], test_size=0.2, random_state=42)

# Initialize Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Sample diet charts, precautions, and tips based on diseases
diet_chart = {
    'COVID-19': ['High-vitamin C foods (oranges, lemons)', 'Warm fluids (soups, herbal teas)', 'Rest and hydration'],
    'Cold': ['Chicken soup', 'Warm fluids', 'Herbal teas', 'Citrus fruits'],
    'Flu': ['Hydration (water, soups)', 'Whole grains', 'Garlic and ginger'],
    'Malaria': ['High-protein foods', 'Bananas', 'Rice and legumes'],
    'Pneumonia': ['High-protein diet', 'Citrus fruits', 'Soup and warm fluids']
}

precautions = {
    'COVID-19': ['Wear a mask', 'Maintain social distancing', 'Frequent hand washing'],
    'Cold': ['Stay warm', 'Avoid close contact with others', 'Stay hydrated'],
    'Flu': ['Get vaccinated', 'Rest and hydrate', 'Avoid public places'],
    'Malaria': ['Use mosquito repellent', 'Sleep under a mosquito net', 'Avoid stagnant water'],
    'Pneumonia': ['Avoid smoking', 'Keep warm', 'Rest and hydrate']
}

tips = [
    "Keep calm and drink water – it's a miracle worker!",
    "A spoonful of honey can soothe your throat, but make sure to wash it down with a cup of tea!",
    "Don't stress – just rest, and let your body do its magic!",
    "Always wash your hands – not only for health, but also to protect your phone from germs!"
]

# Streamlit Title
st.title('Disease Detection Based on Symptoms')

# Input Feature Section (Symptoms Dropdown Menu)
st.sidebar.subheader("Select Symptoms")
selected_symptoms = st.sidebar.multiselect('Select Symptoms', symptoms)

# Prepare input data for prediction
user_input = np.zeros(len(symptoms))
for symptom in selected_symptoms:
    user_input[symptoms.index(symptom)] = 1

# Reshape the input data for prediction
input_data = user_input.reshape(1, -1)

# Make a prediction based on user input
if st.sidebar.button("Predict Disease"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Disease: {prediction[0]}")

    # Medical Report Generation
    st.subheader("Generated Medical Report")
    st.write(f"Disease: {prediction[0]}")
    st.write(f"Symptoms: {', '.join(selected_symptoms)}")
    st.write("Recommendations:")
    
    # Example medical report content (adjust as necessary)
    if prediction[0] == "COVID-19":
        st.write("1. Stay isolated and avoid close contact with others.")
        st.write("2. Monitor your symptoms, especially your breathing.")
        st.write("3. Seek medical attention if symptoms worsen.")
        st.write("4. Stay hydrated and take rest.")
    elif prediction[0] == "Cold":
        st.write("1. Drink plenty of fluids and rest.")
        st.write("2. Over-the-counter medications can help alleviate symptoms.")
        st.write("3. Avoid contact with others to prevent spreading.")
    elif prediction[0] == "Flu":
        st.write("1. Rest and hydrate well.")
        st.write("2. Take over-the-counter flu medication as needed.")
        st.write("3. Contact your doctor if you experience severe symptoms.")
    elif prediction[0] == "Malaria":
        st.write("1. Consult a healthcare professional immediately for anti-malarial treatment.")
        st.write("2. Prevent mosquito bites to avoid further infections.")
    elif prediction[0] == "Pneumonia":
        st.write("1. Get plenty of rest and follow doctor's advice.")
        st.write("2. Take prescribed antibiotics if bacterial pneumonia is diagnosed.")
        st.write("3. Seek immediate medical help if breathing becomes difficult.")

    # Display Diet Chart
    st.subheader("Recommended Diet:")
    st.write(diet_chart[prediction[0]])

    # Display Precautions
    st.subheader("Precautions:")
    st.write(precautions[prediction[0]])

    # Display Funny Tip
    st.subheader("Funny Tip of the Day:")
    st.write(np.random.choice(tips))

    # Feedback Section
    st.subheader("Your Feedback:")
    feedback = st.text_area("Please share your thoughts or suggestions")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")
        st.write(feedback)

# Disease Prediction Graph (based on symptoms selected)
disease_counts = pd.Series(y_pred).value_counts()

# Create animated plot
trace = go.Bar(
    x=disease_counts.index,
    y=disease_counts.values,
    marker=dict(color='rgba(255, 99, 132, 0.6)'),
    text=disease_counts.index
)

layout = go.Layout(
    title="Disease Prediction Counts",
    xaxis=dict(title='Diseases'),
    yaxis=dict(title='Frequency'),
    showlegend=False
)

fig = go.Figure(data=[trace], layout=layout)

# Show the animated graph
st.plotly_chart(fig, use_container_width=True)
