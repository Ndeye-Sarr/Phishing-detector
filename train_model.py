# I trained a model using labeled email examples. The 
# email text was converted into numbers using TF-IDF, 
# then a Logistic Regression model learned to classify 
# emails as phishing or legitimate.

# I split the dataset into training and testing data. I
# trained the model on 80% of the emails and tested it on the 
# remaining 20% to measure how well it could classify emails it hadn't seen before. After evaluating the model, I saved it so the Streamlit application could use it for predictions.
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split # split the dataset into training and testing data 
from sklearn.metrics import accuracy_score


# Load the dataset
df = pd.read_csv("Phishing_Email.csv")

# Remove rows with missing email text or labels
df = df.dropna(subset=["Email Text", "Email Type"])

# X contains the email text
X = df["Email Text"]

# y contains the correct labels
y = df["Email Type"]

# Change the original labels to the labels used by the app
y = y.replace({
    "Safe Email": "legitimate",
    "Phishing Email": "phishing"
})

print("Total emails:", len(df))
print("Unique emails:", df["Email Text"].nunique())

print("\nLabel counts:")
print(y.value_counts())
# Split the data
# 80% is used to train the AI
# 20%(test_size=0.2) is used to test the AI
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42 # make the train and test split the same every time the code is run
)

# Convert the email text into numbers
vectorizer = TfidfVectorizer()

# Learn from the training emails
X_train_numbers = vectorizer.fit_transform(X_train) # learn from the data and transform the training emails into numbers

# Convert the testing emails using the same vectorizer
X_test_numbers = vectorizer.transform(X_test)

# Create the AI model
model = LogisticRegression()

# Train the AI
model.fit(X_train_numbers, y_train)

# Test the AI
predictions = model.predict(X_test_numbers)

# Calculate the accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Save the trained AI model
with open("phishing_model.pkl", "wb") as file: # wb means write in binary mode
    pickle.dump(model, file)

# Save the vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("AI model trained and saved!")

