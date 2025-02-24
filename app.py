import streamlit as st
import pickle
import pandas as pd

# --- Custom CSS for a modern look ---
st.markdown(
    """
    <style>
    /* Change the background color of the main content */
    .main {
        background-color: #f0f2f6;
        color: #333;
    }
    /* Style the sidebar */
    .css-1d391kg {  /* Sidebar container */
        background-color: #f7f7f7;
    }
    /* Customize widget fonts */
    .stTextInput, .stNumberInput, .stSelectbox {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Load the pre-trained pipeline ---
pipe = pickle.load(open('pipe.pkl', 'rb'))

# --- Define teams and cities ---
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# --- Sidebar for user inputs ---
st.sidebar.title("Match Input")
batting_team = st.sidebar.selectbox('Select Batting Team', sorted(teams))
bowling_team = st.sidebar.selectbox('Select Bowling Team', sorted(teams))
selected_city = st.sidebar.selectbox('Select Host City', sorted(cities))
target = st.sidebar.number_input('Target Score', min_value=0, value=150)

st.sidebar.markdown("### Current Score Details")
score = st.sidebar.number_input('Score', min_value=0, value=0)
overs = st.sidebar.number_input('Overs Completed', min_value=0.0, value=0.0, step=0.1)
wickets_out = st.sidebar.number_input('Wickets Out', min_value=0, max_value=10, value=0)

# --- Main App Title ---
st.title('IPL Win Predictor')

# --- Predict Button and Computation ---
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    remaining_wickets = 10 - wickets_out
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [remaining_wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    st.subheader(f"{batting_team} Win Probability: {round(win*100, 2)}%")
    st.subheader(f"{bowling_team} Win Probability: {round(loss*100, 2)}%")
