# DS FastAPI Template
## Iris Example Project

### Deployment URL
- https://fastapi-test.storysquad.dev

### Project Structure
- Project Directory
    - `/application` Python package directory
        - `__init__.py`
        - `data.py` Iris object model for pydantic
        - `main.py` Primary application routes and FastAPI app named `application`
        - `model.joblib` joblib or pickled model
        - `predict.py` Prediction route
    - `.gitignore`
    - `.ebignore`
    - `builder.py` ML model builder script (external)
    - `loader.py` ML model loader script (external)
    - `Procfile` Web app entrypoint
    - `README.md` This file
    - `requirements.txt` Dependencies

### Project Dependencies
- Python 3.7
    - fastapi
    - pydantic
    - uvicorn[standard]
    - joblib
    - pandas
    - scikit-learn
- awscli
- eb

## Setup Instructions - Unix/Linux
In the following steps replace `ds-fastapi-test` with your project's name.

### Local Virtual Environment Setup
```
mkdir ds-fastapi-test
cd ds-fastapi-test
python3.7 -m venv venv
```

### Local Virtual Environment Activation
`source venv/bin/activate`

### Install Local Dependencies
`pip install -r requirements.txt`

### EB - Initialize
`eb init`

### EB - Deploy
`eb create --region us-east-1 ds-fastapi-test`

### EB - Redeploy
`eb deploy ds-fastapi-test`

### EB - Open App
`eb open ds-fastapi-test`

### EB Environment Variables
In the Elastic Beanstalk Console go to your environment -> Configuration. Then
Software -> Edit. At the bottom of the page you can add a [key: value] pair for 
each of the environment variables required for the app.
