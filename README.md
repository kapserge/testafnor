# testafnor
 clonez le repository:
```sh
$ git clone https://github.com/kapserge/testafnor.git

$ cd testafnor
```
chargement des données dans une base de données SQLite:
```sh
$ python manage.py runscript load_pixar
```
execution application(view API):
```sh
$ python manage.py runserver
```
execution test unitaire(view API):
```sh
$ python manage.py test
```
