from fastapi import APIRouter
from joblib import load
from application.data import Iris


router = APIRouter()
model = load('application/model.joblib')


@router.post('/predict')
async def predict(iris: Iris):
    """<h3>Examples</h3>
    <p>Setosa:</p>
    <pre>
    {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    </pre>
    <p>Versicolor:</p>
    <pre>
    {
        "sepal_length": 7.0,
        "sepal_width": 3.2,
        "petal_length": 4.7,
        "petal_width": 1.4
    }
    </pre>
    <p>Virginica:</p>
    <pre>
    {
        "sepal_length": 6.3,
        "sepal_width": 3.3,
        "petal_length": 6.0,
        "petal_width": 2.5
    }
    </pre>
    """
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    x = iris.to_df()
    y_pred, *_ = model.predict(x)
    y_prob, *_ = model.predict_proba(x)
    return {
        'prediction': lookup[y_pred],
        'confidence': f'{max(y_prob):.1%}',
    }
