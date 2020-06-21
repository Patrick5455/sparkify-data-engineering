Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.

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
