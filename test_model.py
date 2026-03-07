from models.data_loader import load_dataset
from models.preprocessing import clean_text
from models.tfidf_model import apply_tfidf
from models.classification import train_classifier

# Load dataset
df = load_dataset()

# Clean resume text
df["clean_text"] = df["resume_text"].apply(clean_text)

# Apply TF-IDF
X, vectorizer = apply_tfidf(df["clean_text"])

# Labels
y = df["category"]

# Train model
model, accuracy, report = train_classifier(X, y)

print("Model Accuracy:", accuracy * 100)
print(report)