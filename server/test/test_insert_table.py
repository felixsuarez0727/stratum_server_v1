import psycopg2

# Connect to the PostgreSQL database server.

conn = psycopg2.connect(host="localhost", database="luxor", user="luxor", password="luxor", port="5432")

# Get cursor object from the database connection.

cursor = conn.cursor()

#sqlCreateTable = "create table "+ table_stratum +" (id bigint, method varchar(128), params varchar(256), result varchar(256));"
sqlInsertRow  = "INSERT INTO dev_1 values(777, 'mining.test', 'test','True')";

cursor.execute(sqlInsertRow)

conn.commit()

