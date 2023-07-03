# Lambda 1 does insertions into the DBs
import pg8000.native


# Connect to an existing database
with pg8000.native.Connection(host="database-2.c1doqm3wbuwt.us-east-2.rds.amazonaws.com", user="postgres", password="postgres", database="main") as conn:

    # Open a cursor to perform database operations
    res = conn.run("select * from logs")
    print(res)