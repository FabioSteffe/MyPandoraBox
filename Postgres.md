## Postgres

default port : 5432

apps basics:
- sudo -u <user> -i  
- createdb dbname  
- dropdb dbname
- dropdb dbname && createdb dbname

psql basics:
- psql dbname : connect to db
- psql dbname username
- \l : list all db
- \c : connect to a db
- \dt : list of tables
- \d tablename : describe a table
- \q : quit

DBAPI for python : pyscopg2 or asyncpg
```
import psycopg2

conn = psycopg2.connect('dbname=todoapp_development user=amy')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
```

string composition:
```
import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()
```

fetching:
'''
cursor.execute('SELECT * FROM table')
cursor.fetchone()
cursor.fetchmany(3)
cursor.fetchall()
'''













