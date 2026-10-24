from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

log_reg = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

knn = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier())
])

decision_tree = DecisionTreeClassifier(random_state=42)

models = {
    "Logistic Regression": log_reg,
    "KNN": knn,
    "Decision Tree": decision_tree
}

print("Baseline Models Accuracy:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}: {accuracy:.4f}")

hard_voting = VotingClassifier(
    estimators=[
        ("lr", log_reg),
        ("knn", knn),
        ("dt", decision_tree)
    ],
    voting="hard"
)

hard_voting.fit(X_train, y_train)
hard_pred = hard_voting.predict(X_test)
hard_accuracy = accuracy_score(y_test, hard_pred)

print("\nHard Voting Classifier Accuracy:")
print(f"{hard_accuracy:.4f}")

soft_voting = VotingClassifier(
    estimators=[
        ("lr", log_reg),
        ("knn", knn),
        ("dt", decision_tree)
    ],
    voting="soft"
)

soft_voting.fit(X_train, y_train)
soft_pred = soft_voting.predict(X_test)
soft_accuracy = accuracy_score(y_test, soft_pred)

print("\nSoft Voting Classifier Accuracy:")
print(f"{soft_accuracy:.4f}")