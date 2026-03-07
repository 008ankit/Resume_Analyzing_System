from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def train_classifier(X, y):

    # Stratified split keeps category distribution balanced
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.15,      # more training data
        random_state=42,
        stratify=y
    )

    # Optimized SVM
    model = LinearSVC(
        C=1.5,
        class_weight="balanced",
        max_iter=5000
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(y_test, predictions)

    return model, accuracy, report