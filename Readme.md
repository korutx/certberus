# Certberus app


## Make virtualenv

On Linux::

```
$ ./manage init
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
(venv3)$ .manage migrate
```


## Make admin user

```
(venv3)$ .manage createsuperuser
```

## runserver

```
(venv3)$ .manage runserver [args]
```