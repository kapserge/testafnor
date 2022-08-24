# testafnor
 clonez le repository:
```sh
$ git clone https://github.com/kapserge/testafnor.git

$ cd testafnor
```
chargement  des données csv dans une base de données SQLite:
```sh
$ python manage.py runscript load_pixar
```
execution l'application(view API):
```sh
$ python manage.py runserver
```
execution du test unitaire(view API):
```sh
$ python manage.py test
```
