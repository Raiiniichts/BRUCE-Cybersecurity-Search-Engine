# BRUCE Cybersecurity Database Search Engine

The BRUCE Engine is a database search function that allows a user to search for a large number of cybersecurity courses through the domain bruce.ist.psu.edu. A search can return many courses in the area of cybersecurity. Each search result contains information such as professor, university, and textbook. It also includes a link to the course syllabus website and a screenshot preview of what the website looks like.

## Process



### Data Gathering



### Course Filtering



### Feature Classification


### Working with MongoDB
For the purposes of this project, MongoDB is quite simple to use. Once you've uploaded the CSV to the bruce server, only a few steps before the database can be built. Perhaps the easiest way to combine the existing csv with the new data is to use cat.

```
cat collection1.csv  collection2.csv > newcollection.csv
```

After you've combined the csv, MongoDB has an easy way to import the csv into a collection.
```
mongoimport --db users --collection contacts --type csv --headerline --file /opt/backups/contacts.csv
```

After you've successfully imported the csv, MongoDB should print out the # of documents you've loaded into the collection.
You can access the collection and look at its contents by following these commands.
```
mongo
show collections
use users (or whatever database the collection is stored in)
db.collection.find() (where collection is the name of the collection)
```

It's important to INDEX the collection now so that the test.php file can properly search in the collection.
An example of an index command. You should read more about it at https://docs.mongodb.com/manual/indexes/
```
db.coursecollection.createIndex(
   {
     DOMAIN: "text",
     TITLE: "text",
   }
 )
```


## Built With

* MongoDB
* PHP
* HTML/CSS


## Authors

* **Andrew Yang** - *Initial work* - *Summer 2018 - Spring 2019*
* **Weiqin Wang** - *Initial work* - *Summer 2018 - Spring 2019*


## Acknowledgments

Thanks to Dongwon Lee for overseeing this project.

