# OnlineShop

## Run worker 
```console
$ celery -A core worker -l info
```
## Run flower
```console
$ celery -A core flower
```
## Run flower and authentificate
```
$ celery -A core flower --basic-auth=username:password
```
