from fastapi import APIRouter
from joblib import load
from application.data import Iris


router = APIRouter()
model = load('application/model.joblib')


@router.post('/predict')
async def predict(iris: Iris):
    """ Examples
    Setosa: [5.1, 3.5, 1.4, 0.2]
    /predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2

    Versicolor: [7.0, 3.2, 4.7, 1.4]
    /predict?sepal_length=7.0&sepal_width=3.2&petal_length=4.7&petal_width=1.4

    Virginica: [6.3, 3.3, 6.0, 2.5]
    /predict?sepal_length=6.3&sepal_width=3.3&petal_length=6.0&petal_width=2.5
    """
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    x = iris.to_df()
    y_pred, *_ = model.predict(x)
    y_prob, *_ = model.predict_proba(x)
    return {
        'prediction': lookup[y_pred],
        'confidence': f'{100 * max(y_prob):.2f}%',
    }
