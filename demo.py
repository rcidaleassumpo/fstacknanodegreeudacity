import psycopg2

# open a connection..
conn = psycopg2.connect('dbname=nanodegreedb')

# get a hold of a cursor. 
cursor = conn.cursor()



# execute changes to database with .execute
cursor.execute("""
    CREATE TABLE todos (
        id serial PRIMARY KEY,
        description VARCHAR NOT NULL
    );
""")


# commit to commit the changes that we made.
conn.commit()

# close the cursor since psql won't close automatically
cursor.close()

# close the connection for the same reason...
conn.close()


# Takeaways:
# First you connect to a database passing the database name, and a optional user name
# Then you get a hold of a cursor, to execute changes to the database
# Then when you are done, you use that connection and call commit.
# Then you clean up, by closing both the cursor and connection. 


