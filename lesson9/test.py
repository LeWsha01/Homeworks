import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Vlad2010",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="testdb")

    cursor = connection.cursor()

    create_table_shops = '''
    CREATE TABLE shops
          (id INTEGER PRIMARY KEY     NOT NULL,
          name           varchar ,
          address        varchar,
          staff_amount     integer); 

    CREATE TABLE departments
          (id INTEGER PRIMARY KEY     NOT NULL,
          sphere          varchar,
          staff_amount    varchar,
          shop            integer,
          FOREIGN KEY(shop) REFERENCES shops(id) );
    
    CREATE TABLE items
          (id INTEGER PRIMARY KEY     NOT NULL,
          name            varchar,
          description        text,
          price            integer,
          department       integer,
          FOREIGN KEY(department) REFERENCES departments(id) );'''

    cursor.execute(create_table_shops)
    connection.commit()
    print("Tables created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")