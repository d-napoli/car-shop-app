# Backend
Backend developed with **Python** (Version 3.9.2)
## Dependencies
- Python
- [Django](https://github.com/d-napoli/tinnova-backend-test/tree/main/5-Cars-API/back-end#download-do-django)
- [Django Rest Framework](https://github.com/d-napoli/tinnova-backend-test/tree/main/5-Cars-API/back-end#download-do-django-rest-framework)
## How to install the project
Download the files from Github <br>
It is always recommended to create a **venv** (Virtual Machine) <br>
In the project folders there is already a **venv** that was used during development <br>
To perform a venv, enter the ` path. / Venv / Scripts` <br>
Run the **activate.bat** file on your <br> terminal
```batch
activate.bat
```
### Download from Python (3.9.2)
Go to the following [link](https://www.python.org/downloads/) and follow the instructions provided by the wizard. <br>
### Why Django?
Django is a **high-level** framework for a Python programming language. It was developed for us to carry out fast, pragmatic and clean development. <br>
Its focus is **productivity, fast delivery and scalable.** <br>
In addition to all these factors, it has a **admin panel** native to your applications.
### Download from Django
Inside our virtual machine (**venv**), we need to install **Django**. <br>
As with virtually all Python packages, we're going to use the **Pip** (Python package index). <br>
```batch
pip install django
```
### Download Django Rest Framework
Inside our virtual machine (**venv **), we need to install **Django Rest Framework**. <br>
```batch
pip install djangorestframework
```
In case of doubt, follow [link](https://www.django-rest-framework.org/) to the official documentation of the **Rest Framework** <br>
### Running the project
After having installed as above mentioned dependencies. <br>
Inside the root of the `backend` folder, run the following command:
```batch
python manage.py runserver
```
If everything is ok, an application will boot to the default path `http://localhost:8000` <br>
### Access the Django Admin Panel
Django has an admin panel natively. To access it, you must have superuser credentials. <br>
To create a **superuser**, just run the following command in the root of the `backend` folder:
```batch
python manage.py makesuperuser
```
Follow the step by step that the terminal will show. <br>
In case of doubt, follow the [link](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) of the official **Django**