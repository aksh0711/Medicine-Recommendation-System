import streamlit as st
import pandas as pd

# Load the dataset
file_path = 'symtoms_df.csv'  # Replace with the actual path
symptoms_df = pd.read_csv(file_path)

# Get the unique list of symptoms
symptom_columns = ['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4']
all_symptoms = pd.unique(symptoms_df[symptom_columns].values.ravel())
all_symptoms = [symptom for symptom in all_symptoms if pd.notna(symptom)]

# Function to predict disease based on symptoms
def predict_disease(selected_symptoms):
    for _, row in symptoms_df.iterrows():
        disease_symptoms = set(row[symptom_columns].dropna())
        if set(selected_symptoms).issubset(disease_symptoms):
            return row['Disease']
    return "Unknown Disease"

# Mock helper function to get details of the predicted disease
def helper(disease):
    details = {
        "Fungal infection": {
            "desc": "A fungal infection affects the skin or mucous membranes.",
            "pre": ["Keep affected area clean", "Use antifungal creams", "Avoid sharing personal items"],
            "med": ["Antifungal medication", "Topical ointments"],
            "die": ["Avoid sugar-rich foods", "Consume probiotics", "Stay hydrated"],
            "wrkout": ["Practice yoga", "Engage in light exercises"],
        },
        # Add more disease details here
        "Unknown Disease": {
            "desc": "No details available.",
            "pre": [],
            "med": [],
            "die": [],
            "wrkout": [],
        },
    }
    return (
        details[disease]["desc"],
        details[disease]["pre"],
        details[disease]["med"],
        details[disease]["die"],
        details[disease]["wrkout"],
    )

# Streamlit UI
st.title("Disease Predictor")

st.write("### Select symptoms from the dropdown menus:")
symptom_1 = st.selectbox("Symptom 1", all_symptoms)
symptom_2 = st.selectbox("Symptom 2", all_symptoms)
symptom_3 = st.selectbox("Symptom 3", all_symptoms)

if st.button("Predict Disease"):
    # Process the selected symptoms
    selected_symptoms = [symptom_1, symptom_2, symptom_3]
    predicted_disease = predict_disease(selected_symptoms)
    desc, pre, med, die, wrkout = helper(predicted_disease)

    # Display results
    st.write("### Predicted Disease")
    st.success(predicted_disease)

    st.write("### Description")
    st.info(desc)

    st.write("### Precautions")
    for p in pre:
        st.write("- " + p)

    st.write("### Medications")
    for m in med:
        st.write("- " + m)

    st.write("### Workout Recommendations")
    for w in wrkout:
        st.write("- " + w)

    st.write("### Dietary Recommendations")
    for d in die:
        st.write("- " + d)
