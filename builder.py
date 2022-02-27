from pandas import DataFrame
from sklearn import svm, datasets
from joblib import dump
from sklearn.model_selection import train_test_split


X, y = datasets.load_iris(return_X_y=True)
df = DataFrame(X, columns=[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
])

X_train, X_test, y_train, y_test = train_test_split(
    df, y,
    test_size=0.2,
    stratify=y,
    random_state=42,
)
model = svm.SVC(
    class_weight='balanced',
    probability=True,
    random_state=42,
)
model.fit(X_train, y_train)
dump(model, 'application/model.joblib')

print(f"Training Accuracy: {model.score(X_train, y_train):.3%}")
print(f"Validation Accuracy: {model.score(X_test, y_test):.3%}")
