import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
# Dataset contains two columns: 'label' and 'message'
# label = 'spam' or 'ham' (ham = not spam)

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv', 
                   sep='\t', names=['label', 'message'])

# Convert labels to binary (spam=1, ham=0)
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label_num'], test_size=0.2, random_state=1)

# Convert text to feature vectors
vectorizer = CountVectorizer()
X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vector, y_train)

# Predict on test set
y_pred = model.predict(X_test_vector)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.2f}%")

# Try a custom message
def predict_message(msg):
    msg_vector = vectorizer.transform([msg])
    prediction = model.predict(msg_vector)[0]
    print("📩 Message:", msg)
    print("🔍 Prediction:", "Spam" if prediction == 1 else "Not Spam")

# Test with sample message
predict_message("Congratulations! You've won a free ticket. Call now!")
predict_message("Hey, are we still meeting at 5?")
