from joblib import load
from pandas import DataFrame
from sklearn import datasets


model = load('application/model.joblib')
X, y = datasets.load_iris(return_X_y=True)
df = DataFrame(X, columns=[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
])
predictions = zip(y, model.predict(df), model.predict_proba(df))
print("pred/y_true: conf")
print("\n".join(f"{pred}/{y_true}: {max(proba):.0%}" for y_true, pred, proba in predictions))
