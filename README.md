This is the reposetory of the Assesment sent by the i-APS team.

You can check a demo of the API here:
https://oltlatifi.pythonanywhere.com/

You can check a quick frontend I pulled up together here:
https://heartfelt-heliotrope-fb9764.netlify.app

## Project Setup

The project was developed and tested using Python 3.10.7

To get started `git clone` the project

### Optional 
>* Create a python virtual enviroment with `python -m venv <name-of-venv>`
>* Activate the virtual enviroment with `<name-of-venv>\Scripts\activate`

Install the project dependencies with `pip install -r requirements.txt`

Navigate to `manage.py`'s directory and run:
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py dataimport`

### Note
`python manage.py dataimport` - imports data from `sample-data.json` and it's for testing purposes only. If you  want to import the whole dataset go to https://www.kaggle.com/datasets/Cornell-University/arxiv and download the whole file. Without renaming it, put it on your base directory and run

>`python manage.py dataimport --full FULL` - this will take a VERY long time.

### Run the project

> `python manage.py runserver`

### API Documentation
Documentation can be found here: https://oltlatifi.pythonanywhere.com//swagger

... or more in depth here:
https://documenter.getpostman.com/view/15122017/2s9Y5SVQbM
