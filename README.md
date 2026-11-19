# AI Phishing Detector

## Project Description

This project is an AI Phishing Detector built with Python and Streamlit. Users can paste an email into the application, and the AI predicts whether the email is **phishing** or **legitimate**.

## Features

- Built a Streamlit user interface.
- Users can paste an email into the application.
- Loaded and explored a phishing email dataset.
- Trained a machine learning model using the dataset.
- Connected the trained AI model to the Streamlit application.
- Predicts whether an email is phishing or legitimate.
- Displays the model's confidence score.
- Identifies potential phishing indicators.
- Evaluates the model using a train/test split and reports its accuracy.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression

## Machine Learning

The application uses:

The application uses:

TF-IDF Vectorizer: Converts email text into numerical features that the model can process.

Logistic Regression: Classifies emails as phishing or legitimate.

80/20 Train-Test Split: Uses 80% of the dataset for training and 20% for evaluating performance on unseen emails.

Accuracy: Measures the percentage of correct predictions.

Precision: Measures how many emails predicted as phishing are actually phishing.

Recall: Measures how many actual phishing emails the model correctly identifies.

F1 Score: Balances precision and recall into a single metric.

Data Preprocessing

The original dataset contained 18,634 email records.

Before training, the dataset was cleaned to remove duplicate emails and resolve one instance where identical email text had conflicting labels.

After preprocessing:

Total unique emails: 17,536

Legitimate emails: 10,979

Phishing emails: 6,557

Model Performance

The model was evaluated on a held-out test set containing 3,508 emails.

Metric

Result

Accuracy

97.95%

Phishing Precision

98.08%

Phishing Recall

96.44%

Phishing F1 Score

97.25%

These results show that the model performs well on the test dataset, although it may still make mistakes when analyzing unfamiliar emails.
## Project Files

- `app.py` – Streamlit application that accepts user input and displays AI predictions.
- `train_model.py` – Loads the dataset, trains the AI model, evaluates its accuracy, and saves the trained model.
- `Phishing_Email.csv` – Dataset used to train the model.
- `phishing_model.pkl` – Saved machine learning model.
- `vectorizer.pkl` – Converts email text into numerical features for the AI model.

## How to Run

1. Install the required libraries.
2. Train the model:

```bash
python train_model.py
```

3. Start the application:

```bash
streamlit run app.py
```

4. Paste an email into the text box.
5. Click **Analyze** to see whether the email is predicted to be **phishing** or **legitimate**, along with the model's confidence score.

## Limitations

- The model predicts based only on the email text.
- It does not verify whether the sender or website is legitimate.
- Some legitimate emails, such as password reset or account verification emails, may be classified as phishing because they use language that is also common in phishing emails.
- The quality of the predictions depends on the quality and diversity of the training dataset.

## Future Improvements

- Analyze the sender's email address and domain.
- Verify whether links belong to trusted domains.
- Improve the user interface.
- Support uploading email files.
- Provide more detailed explanations for each prediction.