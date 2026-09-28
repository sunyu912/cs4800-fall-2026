from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

data = [
    "I love to read books",
    "The quick brown fox jumps",
    "I prefer tea over coffee",
    "Machine learning is an interesting field",
    "Cal Poly Pomona has strong science majors"
]

# Preprocessing the dataset
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)
y = []

for i in range(len(data)):
    words = data[i].split()  # Split the sentence into words
    next_word = words[-1]    # Select the last word as the target
    y.append(next_word)

print(vectorizer.vocabulary_)
print(X)
print(y)

# Initializing and training the SVM model
model = SVC()
model.fit(X, y)

# Example prediction
input_string = "read"
prediction_vector = vectorizer.transform([input_string])
predicted_word = model.predict(prediction_vector)

print(f"The predicted next word after '{input_string}' is: {predicted_word[0]}")
