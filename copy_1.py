import streamlit as st
import joblib

# Load the TF-IDF vectorizer and the trained Random Forest model
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('random_forest_model.pkl')

# Function to predict strategy
def predict_strategy(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Streamlit interface
st.title('Affected aspect')

# Input text area for user to enter text
user_input = st.text_area('Enter text:', '')
import streamlit as st
import joblib

# Load the TF-IDF vectorizer and the trained Random Forest model
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('random_forest_model.pkl')

# Function to predict strategy
def predict_strategy(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Streamlit interface
st.title('Affected aspect')

# Input text area for user to enter text
user_input = st.text_area('Enter text:', '')

# Predict button
if st.button('Ask Here'):
    if user_input.strip() == '':
        st.error('Please enter some text.')
    else:
        prediction = predict_strategy(user_input)
        st.success(f'Predicted Strategy: {prediction}')

# Predict button
if st.button('Ask Here'):
    if user_input.strip() == '':
        st.error('Please enter some text.')
    else:
        prediction = predict_strategy(user_input)
        st.success(f'Predicted Strategy: {prediction}')
