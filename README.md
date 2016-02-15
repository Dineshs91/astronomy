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

## Time conversion
```datetime.strptime('01/01/1880 12:00:00 AM', '%m/%d/%Y %I:%M:%S %p')```

## Start python development server

```$ python manage.py runserver```

## Python shell

```$ python manage.py shell```