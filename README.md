# Astronomy api

Data obtained from [nasa](https://data.nasa.gov/view/ak9y-cwf9)

Powered by Django and Django rest framework.

## Api

**Note:** A trailing slash is always expected.

#### Get all meteorites
```http://127.0.0.1:8000/v1/meteorites/ ```

#### Get a meteorite with its id.
```http://127.0.0.1:8000/v1/meteorites/12/ ```

##Import from csv:

    python manage.py makemigrations
    python manage.py migrate


## Remove /ueff from Meteorite.csv
```sed $'s/\xEF\xBB\xBF//' < Meteorite_Landings.csv > Meteorite.csv```

## Convert datetime to python supported format and move id to the beginning
```python convert.py```

Remove the column names from the csv file before importing into csv.
### sqlite3
    $ sqlite3
    > .open db.sqlite3

    > .mode csv
    > .import Meteorite_sanitized.csv meteorite

### mongodb
    mongoimport --db astronomydb --collection meteorite --type csv --headerline --file Meteorite_sanitized.csv

This will read the contents from Meteorite.csv and writes the new content in Meteorite_sanitized.csv

## Start python development server

```$ python manage.py runserver```

## Python shell

```$ python manage.py shell```
