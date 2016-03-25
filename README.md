#chimera

## requirements

* Python 3.4
* [Firefox 45] (http://www.mozilla.org/firefox)
* [virtualenvwrapper] (http://virtualenvwrapper.readthedocs.org/en/latest/) *optional*

## installation

``` sh
git clone git@github.com:bcfurtado/chimera.git
cd chimera
mkvirtualenv $(cat .virtual-environment) -p $(which python3)
pip install -r requirements.txt
```

## running

### migrations
```sh
python manage.py migrate
```

### tests

```sh
python manage.py test
python manage.py test functional_tests
```

### application
```sh
python manage.py runserver
```
