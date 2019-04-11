# BRUCE Cybersecurity Database Search Engine

The BRUCE Engine is a database search function that allows a user to search for a large number of cybersecurity courses through the domain bruce.ist.psu.edu. A search can return many courses in the area of cybersecurity. Each search result contains information such as professor, university, and textbook. It also includes a link to the course syllabus website and a screenshot preview of what the website looks like.

## Process



### Data Gathering



### Course Filtering



### Feature Classification

### Working with MongoDB
For the purposes of this project, MongoDB is quite simple to use. Once you've uploaded the CSV to the bruce server, only a few steps before the database can be built. Perhaps easiest way to combine the existing csv with the new data is to use cat.

```
cat collection1.csv  collection2.csv > newcollection.csv
```

After you've combined the csv, mongoDB has an easy way to import the csv into a collection.
```
mongoimport --db users --collection contacts --type csv --headerline --file /opt/backups/contacts.csv
```



## Built With

* MongoDb
* HTML/CSS


## Authors

* **Andrew Yang** - *Initial work* - *Summer 2018 - Spring 2019*
* **Weiqin Wang** - *Initial work* - *Summer 2018 - Spring 2019*


## Acknowledgments

Thanks to Dongwon Lee for overseeing this project.

