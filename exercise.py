'''
import streamlit as st

# Title of the app
st.title("AI Phishing Detector")

# Description
st.write("Paste an email or message below to check if it may be phishing.")

# Text box
email = st.text_area("Paste your email here:")

# Button
if st.button("Analyze"):
    if email.strip() == "":
        st.warning("Please paste an email first.")
    else:
        st.success("Your email has been received!")
'''
'''
import streamlit as st

st.title("🛡️ AI Phishing Detector")

st.write("Paste an email or a text below and click Analyze.")

email = st.text_area("Email")

# Potential phishing keywords
phishing_keywords = [
    "urgent",
    "click here",
    "verify",
    "password",
    "bank",
    "account suspended",
    "login",
    "winner",
    "claim",
    "limited time"
]

if st.button("Analyze"):

    if email.strip() == "":
        st.warning("Please paste an email.")

    else:
        score = 0 # this is checking the score of the email based on the keywords

        for word in phishing_keywords:
            if word.lower() in email.lower():
                score += 1

        if score >= 2:
            st.error("⚠️ Possible Phishing Email")
        else:
            st.success("✅ Looks Safe")

        st.write("Phishing Score:", score)
'''
