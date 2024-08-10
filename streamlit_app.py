import streamlit as st
import streamlit_shadcn_ui as ui

# Title of the survey
st.title("DatViz Ai User Survey")

# Position/Occupation
st.subheader("What is your current role?")
occupation_options = [
    {"label": "Business Analyst", "value": "Business Analyst"},
    {"label": "Data Analyst", "value": "Data Analyst"},
    {"label": "Statistician", "value": "Statistician"},
    {"label": "Data Scientist", "value": "Data Scientist"},
    {"label": "Teacher/Professor/Lecturer", "value": "Teacher/Professor/Lecturer"},
    {"label": "Scientist", "value": "Scientist"},
    {"label": "University Student", "value": "University Student"},
    {"label": "High School Student", "value": "High School Student"},
    {"label": "Government Employee", "value": "Government Employee"},
    {"label": "NGO Worker", "value": "NGO Worker"},
    {"label": "Other", "value": "Other"}
]
occupation = ui.radio_group(
    options=occupation_options,
    default_value="Other",
    key="occupation_select"
)

# Field of Endeavor
st.subheader("What field do you work in or study?")
field_options = [
    {"label": "Science and Technology", "value": "Science and Technology"},
    {"label": "Arts and Humanities", "value": "Arts and Humanities"},
    {"label": "Business and Economics", "value": "Business and Economics"},
    {"label": "Health and Medicine", "value": "Health and Medicine"},
    {"label": "Social Sciences", "value": "Social Sciences"},
    {"label": "Education", "value": "Education"},
    {"label": "Law and Public Policy", "value": "Law and Public Policy"},
    {"label": "Engineering and Architecture", "value": "Engineering and Architecture"},
    {"label": "Environmental Studies", "value": "Environmental Studies"},
    {"label": "Information Technology", "value": "Information Technology"}
]
field_of_endeavor = ui.radio_group(
    options=field_options,
    default_value="Other",
    key="field_select"
)

# How did you hear about DatViz Ai?
st.subheader("How did you find out about DatViz Ai?")
heard_about_options = [
    {"label": "Facebook", "value": "Facebook"},
    {"label": "Google", "value": "Google"},
    {"label": "LinkedIn", "value": "LinkedIn"},
    {"label": "YouTube", "value": "YouTube"},
    {"label": "Other", "value": "Other"}
]
heard_about = ui.radio_group(
    options=heard_about_options,
    default_value="Other",
    key="heard_about_radio"
)

# Overall Satisfaction
st.subheader("How would you rate your overall experience with DatViz Ai?")
satisfaction_options = [
    {"label": "Excellent", "value": "Excellent"},
    {"label": "Good", "value": "Good"},
    {"label": "Fair", "value": "Fair"},
    {"label": "Poor", "value": "Poor"}
]
satisfaction = ui.radio_group(
    options=satisfaction_options,
    default_value="Fair",
    key="satisfaction_radio"
)

# Influencing Factors
st.subheader("What influenced your rating of DatViz Ai?")
aspects = st.text_area(
    "Please share any specific details or suggestions for improvement:",
    key="aspects_text"
)

# Ease of Generating Visualizations
st.subheader("How easy was it to create visualizations?")
ease_visualization_options = [
    {"label": "Very Easy", "value": "Very Easy"},
    {"label": "Easy", "value": "Easy"},
    {"label": "Neutral", "value": "Neutral"},
    {"label": "Difficult", "value": "Difficult"},
    {"label": "Very Difficult", "value": "Very Difficult"}
]
ease_visualization = ui.radio_group(
    options=ease_visualization_options,
    default_value="Neutral",
    key="ease_visualization_radio"
)

# Ease of Generating Data Insights
st.subheader("How easy was it to get insights from the data?")
ease_insights_options = [
    {"label": "Very Easy", "value": "Very Easy"},
    {"label": "Easy", "value": "Easy"},
    {"label": "Neutral", "value": "Neutral"},
    {"label": "Difficult", "value": "Difficult"},
    {"label": "Very Difficult", "value": "Very Difficult"}
]
ease_insights = ui.radio_group(
    options=ease_insights_options,
    default_value="Neutral",
    key="ease_insights_radio"
)

# Challenges in Generating Visualizations
st.subheader("Did you face any issues while creating visualizations?")
challenges_visualization = st.text_area(
    "Please describe any challenges you faced:",
    key="challenges_visualization_text"
)

# Challenges in Generating Data Insights
st.subheader("Did you face any issues while getting data insights?")
challenges_insights = st.text_area(
    "Please describe any challenges you faced:",
    key="challenges_insights_text"
)

# Accuracy of Visualizations
st.subheader("Were the visualizations useful and accurate?")
accuracy_visualization_options = [
    {"label": "Yes", "value": "Yes"},
    {"label": "Somewhat", "value": "Somewhat"},
    {"label": "No", "value": "No"}
]
accuracy_visualization = ui.radio_group(
    options=accuracy_visualization_options,
    default_value="Somewhat",
    key="accuracy_visualization_radio"
)

# Accuracy of Data Insights
st.subheader("Were the insights useful and accurate?")
accuracy_insights_options = [
    {"label": "Yes", "value": "Yes"},
    {"label": "Somewhat", "value": "Somewhat"},
    {"label": "No", "value": "No"}
]
accuracy_insights = ui.radio_group(
    options=accuracy_insights_options,
    default_value="Somewhat",
    key="accuracy_insights_radio"
)

# Interface Intuitiveness
st.subheader("How easy was the interface to use?")
intuitiveness_options = [
    {"label": "Very Intuitive", "value": "Very Intuitive"},
    {"label": "Intuitive", "value": "Intuitive"},
    {"label": "Neutral", "value": "Neutral"},
    {"label": "Confusing", "value": "Confusing"},
    {"label": "Very Confusing", "value": "Very Confusing"}
]
intuitiveness = ui.radio_group(
    options=intuitiveness_options,
    default_value="Neutral",
    key="intuitiveness_radio"
)

# Issues or Bugs Encountered
st.subheader("Did you encounter any problems or bugs?")
issues_options = [
    {"label": "Yes", "value": "Yes"},
    {"label": "No", "value": "No"}
]
issues = ui.radio_group(
    options=issues_options,
    default_value="No",
    key="issues_radio"
)
if issues == "Yes":
    bug_description = st.text_area(
        "Please describe the issue and attach any error messages if possible:",
        key="bug_description_text"
    )

# Recommendation
st.subheader("Would you recommend DatViz Ai to others?")
recommendation_options = [
    {"label": "Yes", "value": "Yes"},
    {"label": "Maybe", "value": "Maybe"},
    {"label": "No", "value": "No"}
]
recommendation = ui.radio_group(
    options=recommendation_options,
    default_value="Maybe",
    key="recommendation_radio"
)

# Willingness to Subscribe
st.subheader("Would you consider subscribing to DatViz Ai?")
subscription_options = [
    {"label": "Yes", "value": "Yes"},
    {"label": "Maybe", "value": "Maybe"},
    {"label": "No", "value": "No"}
]
subscription = ui.radio_group(
    options=subscription_options,
    default_value="Maybe",
    key="subscription_radio"
)

# Suggestions for Improvement
st.subheader("Do you have any suggestions for improving DatViz Ai?")
suggestions = st.text_area(
    "Please share your ideas for improvement:",
    key="suggestions_text"
)

st.write("")
st.write("")
st.write("")

# Submit Button
if ui.button(text="Submit", key="submit_button"):
    st.success("Thank you for completing the survey!")
