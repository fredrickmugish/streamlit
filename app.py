import streamlit as st
import joblib

# Load the TF-IDF vectorizer and the trained Random Forest model
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('random_forest_model.pkl')

# List of possible conditions
conditions = [
    'blended learning', 'digitization', 
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
# Add CORS headers to allow requests from any origin
@st.cache_data
def predict_strategy(text):
    text_tfidf = tfidf_vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Streamlit interface
st.title('Affected Aspect')

# Define checkboxes content
checkboxes_content = {
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

            # Generate a URL for the predicted strategy
            strategy_page_map = {
                "technology_integration": "technology_integration",
                "blended_learning": "blended_learning",
                "digitization": "digitization",
                "safety_measure": "safety_measure",
                "comprehensive_health_safety_measure": "comprehensive_health_safety_measure",
                "program_curriculum_review_update": "program_curriculum_review_update",
                "continuous_improvement_assessment": "continuous_improvement_assessment",
                "research_experiment_standardization": "research_experiment_standardization",
                "professional_development_plan": "professional_development_plan",
                "enrollment_initiative": "enrollment_initiative",
                "budget_optimization": "budget_optimization",
                "financial_auditing": "financial_auditing",
                "cash_flow_analysis": "cash_flow_analysis",
                "financial_planning": "financial_planning",
                "compliance_management_framework": "compliance_management_framework",
                "transparent_governance_framework": "transparent_governance_framework",
                "missiondriven_policy_alignment": "mission_driven_policy_alignment",
                "security_measure": "security_measure",
                "workforce_planning": "workforce_planning",
                "community_engagement_initiative": "community_engagement_initiative",
                "accommodation_optimization": "accommodation_optimization",
                "strategic_recruitment": "strategic_recruitment",
                "workflow_analysis": "workflow_analysis",
                "mental_health_support_service": "mental_health_support_service"
            }

            strategy_key = prediction.lower().replace(" ", "_")
            if strategy_key in strategy_page_map:
                strategy_url = f"https://inteldss-system.onrender.com/strategies/{strategy_page_map[strategy_key]}"
                st.markdown(f"[Click here to view the recommendations for {aspect}]({strategy_url}) ")
            else:
                st.markdown(f"No direct link available for the strategy: {prediction}")
else:
    st.write("Please enter all the required information.")
