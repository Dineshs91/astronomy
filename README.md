# Astronomy api

Data obtained from [nasa](https://data.nasa.gov/view/ak9y-cwf9)

##Import from csv:

Remove the column names from the csv file before importing into csv.
### sqlite3
    $ sqlite3
    > .open db.sqlite3
CREATE TABLE meteorites(
  "name" text,
  "id" integer,
  "nametype" text,
  "recclass" text,
  "mass" float,
  "fall" text,
  "year" text,
  "reclat" text,
  "reclong" text,
  "geolocation_address" text,
  "geolocation_zip" text,
  "geolocation_city" text,
  "geolocation" text,
  "geolocation_state" text
);
    
    > .mode csv
    > .seperator ,
    > .import Meteorite_sanitized.csv meteorites

### mongodb
    mongoimport --db astronomydb --collection meteorites --type csv --headerline --file Meteorite_sanitized.csv

## Remove /ueff from Meteorite.csv
```sed $'s/\xEF\xBB\xBF//' < Meteorite_Landings.csv > Meteorite.csv```

## Convert datetime to python supported format
```python convert_time.py```

This will read the contents from Meteorite.csv and writes the new content in Meteorite_sanitized.csv

## Start python development server

```$ python manage.py runserver```

## Python shell

```$ python manage.py shell```
