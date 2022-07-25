# __ADDRESS BOOK Backend API__
Address book application where users can create, update and delete addresses. And also retrieve addresses within a given distance and coordinates.


## Create a `venv` virtual environment


```bash
python -m venv venv
source venv/Scripts/activate
```
To deactivate the environment run the following.

```bash
deactivate
```

## Install dependencies

```bash
source venv/Scripts/activate
venv/Scripts/python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirments.txt

```


## Create `.env` file to load Settings

```bash
type nul > .env
```



## Add Google API Key with variable `GOOGLE_API_KEY`



## RUN APPLICATION
```bash
python aplication.py
```
OR

```bash
uvicorn main:application --reload
```

## POSTMAN Collection's all present in the project directory, kindly import it to test APIs.
or
## Use the Swagger API Documentation to test APIs by following url,
`http://localhost:8000/docs`# address-book
