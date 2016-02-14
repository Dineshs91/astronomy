# Astronomy api

Data obtained from [nasa](https://data.nasa.gov/view/ak9y-cwf9)

##Import from csv:

### sqlite3
    $ sqlite3
    > .open db.sqlite3
    > .mode csv
    > .import astronomy/Meteorite.csv meteorites

### mongodb
    mongoimport --db astronomydb --collection meteorites --type csv --headerline --file Meteorite.csv

## Remove /ueff from Meteorite.csv
```sed $'s/\xEF\xBB\xBF//' < Meteorite_Landings.csv > Meteorite.csv```


## Start python development server

```$ python manage.py runserver```