### Abstract
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app In order to achive this, they need to prepare a proper data model with approproate contrainst to make the data easy available and maintain integrity of the data.


### The Schema:
The name of the database is sparkifydb using the Postgres sql falvour and psycopg2 as the Python wrapper.
The dataabse was modelled using Fact & Dimension Tables. 

> Fact Table:
>> songplays
> Dimension Tables:
>> users
>> songs
>> artists
>> time

`NOT NULL CONSTRAINTS`

In the fact table, NOT NULL contrains were placed on the user_id and start_time (both foreign keys) to  any entry where there is either no user or session (no start time) in the fact table.

`CONFLICT CONSTRAITS`
he INSERT statements handle the ON CONFLICT scenarios as appropriate. The level of a user is being modified upon any UPDATE request, rest are just ignored as most of the others are static data, which are very unlikely to change.


`RUNNING THE SCRIPTS`
The first script to run is the create_tables.py which would first connect to the host databse and then create a new one called sparkifydb that would be used for the project
THe script when run would also run the creat_table queries from the sql_queries imported in the create_tables.py script

Next, the etl.py script can then be ran.
This would access the folders using the OS module and process each filepath and insert values from the json files to their corresponding tables.

`OTHER SCRIPTs`
> The etl.ipynb,test.ipynb and view.ipynb are used for development purposes. The etl.ipynb is used to test how the data would be accessed from the filepath and how data from the files would be inserted into the tables.
> The test.ipynb script is used  to view the results of etl.ipynb whether data was actaully inserted.
> THe view.ipynb is where pandas was used to access the files and get more conversant with the data been processed. 




Steps:
> I started by defining the SQL queries to create tables, 
drop tables, insert tables and query records from existing tables 

Some of the queries include:

time_table_create = (""" CREATE TABLE IF NOT EXISTS time 
                          (start_time TIMESTAMP PRIMARY KEY, 
                          hour INTEGER,
                          day INTEGER,
                          week INTEGER,
                          month INTEGER,
                          year INTEGER,
                          weekday INTEGER);
                          """)


> Next, I created another file named create_tables.py that was used to connect to the local instance of postgresql on my local machine and I imported sql_queries.py file to exexcute the already definced queries

> Next, I created another file that was called etl.py where I defined functions with python inbuilt os function and pandas to collect data files and parse these json files to pandas for further processing into the databse using the alredy defined sql queries imported with the sql_queries file.

> Finally I used forloop and certain functions in the python os module to traverse through each file and process the file as data inserted to the database. 

> The various data contained in all 77 json files were inserted succesfully into the databsse. 
