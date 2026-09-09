# strip will remove the extra spaces in the email that the user pasted
# import streamlit so we can build a web application 
import streamlit as st
import pickle  # import pickle so we can load the AI model that was trained in train_model.py. Pickle is used to save and load Python objects

# Load the saved AI model and vectorizer
with open("phishing_model.pkl", "rb") as file: # open the AI model file. rb means read in binary mode, the model is stored as binary data
    # load the trained model into the variable named model
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file: # open the saved vectorizer file. the vectorizer will convert the text into numbers
    # load the vectorizer into the varibale named vectorizer
    vectorizer = pickle.load(file)
    #st.write(model.classes_)
# display the title of the web page
st.title("🛡️ AI Phishing Detector")

st.write("Paste an email or a text message that you think might be"
         " suspicious and the AI will analyze it to determine if it is a phishing attempt or not.")

# the text area where the users can paste an email or a text that they might think is suspicious
email = st.text_area("Paste an email or a text message here:")

# when the user click the analyze button, the if statement runs
if st.button("Analyze"):
    # check if the user has pasted nothing
    if email.strip() == "":
        # if the user did not paste anything, then the warning message will be displayed 
        st.warning("Please paste an email or a text message.")
    else:
        # otherwise convert the email into nubers, the AI cannot understand words directky so it has to be converted to numbers
        email_numbers = vectorizer.transform([email]) #transform the email into numbers using the vectorizer
        # the trained model will predict if the email is either phishing or not

        prediction = model.predict(email_numbers)[0] # [0] is used to get the first and only prediction
     
        
        probabilities = model.predict_proba(email_numbers)[0] # get the probability of the prediction, the model will return two probabilities, one for phishing and one for legitimate

        legitimate_probability = probabilities[0] # first is legitimate 
        phishing_probability = probabilities[1] # second is phishing
        
        reasons = [] 
        if "http" in email.lower():
            reasons.append("Contains a link.")

        if "password" in email.lower():
            reasons.append("Mentions a password.")

        if "verify" in email.lower():
            reasons.append("Requests account verification.")

        if "urgent" in email.lower() or "immediately" in email.lower():
            reasons.append("Uses urgent language.")

        if "click" in email.lower():
            reasons.append("Asks the user to click a link.")

        st.divider()
        # display the result to the user
        if prediction == "phishing":
            confidence = int(phishing_probability * 100)

            st.error(f"⚠️ This email may be phishing with a confidence of {confidence}%.") # st.error display a red message

            if reasons:
                st.write("Potential phishing indicators found:")
                for reason in reasons:
                    st.write(f"- {reason}")   
        else:
            confidence = int(legitimate_probability * 100)

            st.success(f"✅ This email looks legitimate with a confidence of {confidence}%.") # st.success display a green message

         
st.info(
    "This prediction is based on the email text only. "
    "Always verify the sender and any links before taking action."
)                