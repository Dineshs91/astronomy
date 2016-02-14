# Astronomy api

Data obtained from [nasa](https://data.nasa.gov/view/ak9y-cwf9)

Db path: ~/Library/Application Support/Astronomy/db

```mongod --dbpath ~/Library/Application\ Support/astronomy/db```

##Import from csv:

```mongoimport --db astronomydb --collection meteorites --type csv --headerline --file Meteorite.csv```

## Remove /ueff from Meteorite.csv
```sed $'s/\xEF\xBB\xBF//' < Meteorite_Landings.csv > Meteorite.csv```
