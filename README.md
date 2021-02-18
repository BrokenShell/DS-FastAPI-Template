# DS FastAPI Template
## Iris Example Project

### Deployment URLs
- Heroku: https://fastapi-template.herokuapp.com
- AWS: https://fastapi-test.storysquad.dev/

### Project Structure
- `/ds-fastapi-test/` Project Directory
    - `/application/` Python package directory
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
    - `runtime.txt` Specifies Python version

### Project Dependencies
- Python 3.7.10
    - fastapi
    - pydantic
    - uvicorn[standard]
    - joblib
    - pandas
    - scikit-learn
- awscli
- eb

## Setup Instructions - Unix/Linux or Windows with WSL
In the following steps replace `ds-fastapi-test` with your project's name.

### Local Virtual Environment Setup
```shell
mkdir ds-fastapi-test
cd ds-fastapi-test
python3.7 -m venv venv
```

### Local Virtual Environment Activation
```shell
source venv/bin/activate
```

### Install Local Dependencies
```shell
pip install -r requirements.txt
```

### Run App Locally
```shell
uvicorn application:application
```

### Elastic Beanstalk - Initialize
```shell
eb init
```
This is an interactive prompt. It will ask you a series of questions about your project.
For more details - refer to this walk through: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html

### Elastic Beanstalk - Deploy
```shell
eb create --region us-east-1 ds-fastapi-test
```

### Elastic Beanstalk - Redeploy
```shell
eb deploy ds-fastapi-test
```

### Elastic Beanstalk - Open App
```shell
eb open ds-fastapi-test
```

### Elastic Beanstalk Environment Variables
In the Elastic Beanstalk Console go to your environment -> Configuration. Then
Software -> Edit. At the bottom of the page you can add a [key: value] pair for 
each of the environment variables required for the app.
