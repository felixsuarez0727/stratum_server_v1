import psycopg2

def create_dev_table()

  # Connect to the PostgreSQL database server.

  conn = psycopg2.connect(host="localhost", database="luxor", user="luxor", password="luxor", port="5432")
  table_stratum = "dev_1"

  # Get cursor object from the database connection.

  cursor = conn.cursor()
  sqlCreateTable = "create table "+ table_stratum +" (id bigint, method varchar(128), params varchar(256), result varchar(256));"

  # Insert statement.

  cursor.execute(sqlCreateTable)
  conn.commit()

