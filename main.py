import streamlit as st

# Set the page configuration for layout and title
st.set_page_config(page_title="MEDITRON", layout="wide")

# Add a hello message to greet the user
st.markdown("<h1 style='text-align: left;'>Welcome to MEDITRON 🏥</h1>", unsafe_allow_html=True)
st.markdown("""
    Hello there! We are here to assist you with predicting diseases based on symptoms, AI-based X-ray diagnoses, 
    and providing detailed health reports. Choose a feature below to get started!
""")

# Interactive Feature Section with Colorful Boxes (one per line)
st.markdown("<h3 style='text-align: left;'>Select the feature you want to explore:</h3>", unsafe_allow_html=True)

# Feature boxes (scaled up and one per line)
st.markdown("""
    <div style="background-color:#f4a261; padding:20px; border-radius:10px; font-size:22px; color:white; margin-bottom:15px; text-align:center;">
        👩‍⚕️ Disease Detection
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color:#2a9d8f; padding:20px; border-radius:10px; font-size:22px; color:white; margin-bottom:15px; text-align:center;">
        🩻 X-Ray Examination
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color:#264653; padding:20px; border-radius:10px; font-size:22px; color:white; margin-bottom:15px; text-align:center;">
        💬 Medical Chatbot
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color:#e76f51; padding:20px; border-radius:10px; font-size:22px; color:white; margin-bottom:15px; text-align:center;">
        📄 Report Generator
    </div>
""", unsafe_allow_html=True)

# Add an attractive image with a welcoming message
st.markdown("<h4 style='text-align: left;'>Let's make healthcare smarter and easier! 💡</h4>", unsafe_allow_html=True)

# Health Tips Scrolling Line at the Bottom (slowed down and no gap)
st.markdown("""
    <style>
        .health-tips {
            width: 100%;
            overflow-x: hidden;
            white-space: nowrap;
            position: fixed;
            bottom: 0;
            left: 0;
            background-color: #f1faee;
            padding: 10px;
        }
        .health-tips div {
            display: inline-block;
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-right: 50px;
        }
        .health-tips-wrapper {
            animation: scrollLeft 60s linear infinite;  /* Slowed down the speed */
        }
        @keyframes scrollLeft {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-100%);
            }
        }
    </style>
    <div class="health-tips">
        <div class="health-tips-wrapper">
            🏥 Health Tip: Stay hydrated and get enough sleep to maintain a strong immune system! 💪 | 🧑‍⚕️ Health Tip: Regular exercise can help prevent many diseases! 🚶‍♂️ | 🥗 Health Tip: Eat a balanced diet for better overall health! 🥦 | 🧘‍♀️ Health Tip: Meditation can reduce stress and improve mental health! 🌿 | 🍎 Health Tip: Eating fruits regularly can boost your immune system! 🍓 | 🚶‍♀️ Health Tip: Take daily walks for better heart health! ❤️ | 🧴 Health Tip: Always wash your hands regularly to avoid infections! 🧼 | 💊 Health Tip: Don’t skip your regular medical checkups to stay healthy! 🩺
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer Section with contact information
st.markdown("""
    ---  
    💬 **Contact Us:**  
    Email: support@meditron.com  
    Follow us on [Twitter](https://twitter.com/MEDITRON)
""")
