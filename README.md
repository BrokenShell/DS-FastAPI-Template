# DS FastAPI Template


### Deployment URLs
- Todo

### Project Structure
- Project Directory
    - `/application` - Python package
        - `__init__.py` - `from application.main import application`
        - `data.py` - Iris object model
        - `main.py` - primary application routes and FastAPI app named `application`
        - `model.joblib` - joblib or pickled model
        - `predict.py` - predict route
    - `.gitignore`
    - `.ebignore`
    - `builder.py` - ML model builder script (external)
    - `loader.py` - ML model loader script (external)
    - `README.md` - This file
    - `requirements.txt` - Dependencies


### The deployment should include only the following
- Python package: `/application`
- Project dependencies: `requirements.txt`


### Iris Example Project Dependencies
- FastAPI
- pydantic
- uvicorn[standard]
- joblib
- pandas
- scikit-learn


### EB Environment Variables
In the Elastic Beanstalk Console go to your environment -> Configuration. Then
Software -> Edit. At the bottom of the page you can add a [key: value] pair for 
each of the environment variables required for the app.

### EB Initialize
`eb init`

### EB Deploy
`eb create --region us-east-1 ds-fastapi-test`

### EB Redeploy
`eb deploy ds-fastapi-test`
