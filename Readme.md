# Certberus app


## Make virtualenv

On Linux::

```
$ python3 -m virtualenv venv3
$ . venv3/bin/activate
(venv)$ pip install -r requirements.txt
```

On Windows::

```
> python -m venv venv3
> venv3/Scripts/activate
(venv3)$ pip install -r requirements.txt
```


## migrate

```
(venv3)$ cd certberus 
(venv3)$ python manage.py migrate
```


## Make admin user

```
(venv3)$ python manage.py createsuperuser
```

## runserver

```
(venv3)$ cd certberus 
(venv3)$ python manage.py runserver
```