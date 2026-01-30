from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from services.classification.classifier import TicketClassifier


class MLClassifier(TicketClassifier):
    """
    Supervised ML classifier using TF-IDF + Logistic Regression.
    """

    def __init__(self):
        self.pipeline = Pipeline(
            steps=[
                ("tfidf", TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2)
                )),
                ("model", LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced"
                )),
            ]
        )
        self.trained = False

    def train(self, descriptions, labels):
        X_train, X_test, y_train, y_test = train_test_split(
            descriptions,
            labels,
            test_size=0.2,
            random_state=42,
            stratify=labels
        )

        self.pipeline.fit(X_train, y_train)
        self.trained = True

        predictions = self.pipeline.predict(X_test)

        print("\nML CLASSIFIER EVALUATION")
        print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
        print(classification_report(y_test, predictions))

    def classify(self, description: str) -> str:
        if not self.trained:
            raise RuntimeError("MLClassifier must be trained before use.")

        return self.pipeline.predict([description])[0]
