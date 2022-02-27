# BloomTech Data Science FastAPI Template
## Iris Example Project

### Deployment URLs
- Heroku: https://fastapi-template.herokuapp.com

### Project Structure
- `/ds-fastapi-test/` Project Directory
    - `/application/` Python package directory
        - `__init__.py`
        - `data.py` Iris object model for pydantic
        - `main.py` Primary application routes and FastAPI app named `application`
        - `model.joblib` serialized ML model
        - `predict.py` Prediction route
    - `.gitignore`
    - `.ebignore`
    - `builder.py` ML model builder script (external)
    - `loader.py` ML model loader script (external)
    - `Procfile` Web app entrypoint
    - `README.md` This file
    - `requirements.txt` Dependencies
    - `run_dev_srv.sh` Run script for developer mode
    - `run_pro_srv.sh` Run script for production mode (matches Procfile)
    - `runtime.txt` Specifies Python version (Heroku)

### Project Dependencies
- Python 3.7.x
    - fastapi
    - pydantic
    - joblib
    - pandas
    - scikit-learn
    - uvicorn[standard] (development server)
    - gunicorn (production server)
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

### Run App in Developer Mode (Linux or Mac)
```shell
./run_dev_srv.sh
```

### Run App in Production Mode (Linux or Mac)
```shell
./run_prod_srv.sh
```

# Deployment Options

## 1. Heroku Deployment
- Push project to GitHub
- Use Heroku's GitHub integration
- Deploy App
- Environment Variables
  - In the Heroku Console go to your app `settings` tab
  - Click `Reveal Config Vars` button
  - Add a [key: value] pair for each environment variable

## 2. AWS Elastic Beanstalk Deployment

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
