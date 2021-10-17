# django-101

## Get started
1. Install python3
```
$ brew install python3
```
2. Create virtual environment of python
```
$ python3 -m venv ENV
$ source ENV/bin/activate
```
3. Create rquirement file to list library
```
$ pip freeze > requirements.txt
```
use this command for install library from requirements file
```
$ pip install -r requirements.txt
```
4. Create django project
```
$ pip install django
$ django-admin startproject <project name> .
```
5. Run project
```
$ ./manage.py runserver
```


