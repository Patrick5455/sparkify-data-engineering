import psycopg2
from psycopg2 import Error as e
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    """
    Run #sudo service postgresql restart on terminal,
    if program throws up error on terminal that database could not be dropped 
    becuase another user is using the session.
    
    """
    
    try:
      # connect to default database
      conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
      conn.set_session(autocommit=True)
      cur = conn.cursor()
      print('connected')

      # create sparkify database with UTF8 encoding
      cur.execute("DROP DATABASE IF EXISTS sparkifydb")
      print("DATABASE DROPED")
      cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
      print("database created")

      # close connection to default database
      conn.close()    
      # connect to sparkify database
      conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
      cur = conn.cursor()
      
    except e:
      print("error in creating database")
      print(e.pgerror)
    
    #print("cursor and conection returned")
    return cur, conn
    


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    try:
      for query in drop_table_queries:
          cur.execute(query)
          conn.commit()
    except e:
      print("error in dropping tables")


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    try:
      for query in create_table_queries:
          cur.execute(query)
          conn.commit()
      print("tables created")
    except:
      print("error in creating tables")
    


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print("queries successful")


if __name__ == "__main__":
    main()