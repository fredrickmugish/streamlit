import streamlit as st
import joblib

# Load the TF-IDF vectorizer and the trained Random Forest model
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('random_forest_model.pkl')

# List of possible conditions
conditions = [
    'technology integration', 'blended learning', 'digitization', 
    'safety measure', 'technology integration', 
    'comprehensive health safety measure', 'program curriculum review update', 
    'continuous improvement assessment', 'research experiment standardization', 
    'professional development plan', 'enrollment initiative', 
    'budget optimization', 'financial auditing', 'cash flow analysis', 
    'financial planning', 'compliance management framework', 'transparent governance framework', 
    'missiondriven policy alignment', 'security measure', 'workforce planning', 
    'community engagement initiative', 'accommodation optimization', 'strategic recruitment', 
    'workflow analysis', 'mental health support service'
]

# Create a mapping from condition names to their indices
condition_to_index = {condition: index for index, condition in enumerate(conditions)}

# Function to predict strategy
def predict_strategy(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Streamlit interface
st.title('Affected Aspect')

# Define checkboxes content
checkboxes_content = {
    "Infrastructure and Resources": False,
    "Learning Environment": False,
    "Access to Resources": False,
    "Facilities Safety": False,
    "Technology Infrastructures": False,
    "Physical Health and Safety": False,
    "Educational Programs and Curriculum": False,
    "Quality Assurance": False,
    "Research and Experiments": False,
    "Employee Development and Training": False,
    "Students Enrollment": False,
    "Budget Allocation": False,
    "Running Cost": False,
    "Debt": False,
    "Tuition and Fee Setting": False,
    "Legal and Regulatory Compliance": False,
    "Governance Structure": False,
    "Mission, Vision, and Values": False,
    "Cyber Crime": False,
    "Workforce Planning and Analysis": False,
    "Social Connections and Community Engagement": False,
    "Students Accommodation": False,
    "Recruitment": False,
    "Administrative Functions": False,
    "Mental Health and Emotional Well-being": False,
}

# Split the checkboxes into three columns
num_checkboxes = len(checkboxes_content)
column_size = num_checkboxes // 3

# Create three columns
col1, col2, col3 = st.columns(3)

# Input checkboxes for each aspect in each column
with col1:
    user_input_col1 = {key: st.checkbox(key, value, key=f"{key}_col1") for key, value in list(checkboxes_content.items())[:column_size]}
with col2:
    user_input_col2 = {key: st.checkbox(key, value, key=f"{key}_col2") for key, value in list(checkboxes_content.items())[column_size:2*column_size]}
with col3:
    user_input_col3 = {key: st.checkbox(key, value, key=f"{key}_col3") for key, value in list(checkboxes_content.items())[2*column_size:]}

# Merge user inputs from all columns
user_input = {**user_input_col1, **user_input_col2, **user_input_col3}

# Predict button
if st.button('Ask Here', type="primary"):
    selected_aspects = [key for key, value in user_input.items() if value]
    if not selected_aspects:
        st.error('Please select at least one aspect.')
    else:
        # Display the predicted strategy for each selected aspect
        for aspect in selected_aspects:
            # Combine selected aspect into text
            text = f"- [x] {aspect}"
            # Predict strategy based on the text
            prediction = predict_strategy(text)
            # Display the predicted strategy for the aspect
            st.success(f'Strategy for {aspect}: {prediction}')

        # Get the index of the predicted condition
        predicted_index = condition_to_index.get(prediction)
        if predicted_index is not None:
            st.write(f"Based on your input, you might be experiencing symptoms related to *{conditions[predicted_index]}*.")
        else:
            st.write("The prediction is not recognized.")
else:
    st.write("Please enter all the required information.")
