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
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# Load the dataset
df = pd.read_csv("Phishing_Email.csv")

# Remove rows with missing email text or labels
df = df.dropna(subset=["Email Text", "Email Type"])

# Find email texts that have conflicting labels
label_counts = df.groupby("Email Text")["Email Type"].nunique()
conflicting_texts = label_counts[label_counts > 1].index

print("Repeated emails with conflicting labels:", len(conflicting_texts))

# Remove ambiguous emails, then remove repeated copies
df = df[~df["Email Text"].isin(conflicting_texts)]
df = df.drop_duplicates(subset=["Email Text"])

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

# Calculate the metrics
accuracy = accuracy_score(y_test, predictions)
phishing_precision = precision_score(
    y_test, predictions, pos_label="phishing", zero_division=0
)
phishing_recall = recall_score(
    y_test, predictions, pos_label="phishing", zero_division=0
)
phishing_f1 = f1_score(
    y_test, predictions, pos_label="phishing", zero_division=0
)

print(f"Accuracy: {accuracy:.2%}")
print(f"Phishing precision: {phishing_precision:.2%}")
print(f"Phishing recall: {phishing_recall:.2%}")
print(f"Phishing F1 score: {phishing_f1:.2%}")
print("\nFull report:")
print(classification_report(y_test, predictions, zero_division=0))

# Save the trained AI model
with open("phishing_model.pkl", "wb") as file: # wb means write in binary mode
    pickle.dump(model, file)

# Save the vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("AI model trained and saved!")

