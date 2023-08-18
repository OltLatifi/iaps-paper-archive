This is the reposetory of the Assesment sent by the i-APS team.

## Project Setup

To get started `git clone` the project

### Optional 
>* Create a python virtual enviroment with `python -m venv <name-of-venv>`
>* Activate the virtual enviroment with `<name-of-venv>\Scripts\activate`

Install the project dependencies with `pip install -r requirements.txt`

Navigate to `manage.py`'s direcotry and run:
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py dataimport`

### Note
`python manage.py dataimport` - imports data from `sample-data.json` and it's for testing purposes only. If you  want to import the whole dataset go to https://www.kaggle.com/datasets/Cornell-University/arxiv and download the whole file. Without renaming it, put it on your base directory and run

>`python manage.py dataimport --full FULL` - this will take a VERY long time.

### Run the project

> `python manage.py runserver`
