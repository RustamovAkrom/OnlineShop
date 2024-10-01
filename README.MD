# OnlineShop

## Runing project

### Install dependenciase
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt

```
### Run Redis
```console
$ systemctl start redis-server
```
### Run Celery
```console
$ celery -A core worker -l info
```
### Run flower
```console
$ celery -A core flower
```
### Run flower and authentificate
```
$ celery -A core flower --basic-auth=username:password
```
### Run
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python mangae.py runserver
```