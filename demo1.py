import psycopg2

conn = psycopg2.connect('dbname=nanodegreedb')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS table2;")

cursor.execute("""
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    );
""")

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False
}

cursor.execute(SQL, data)

conn.commit();

conn.close()
cursor.close()
