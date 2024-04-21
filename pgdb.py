import psycopg2
from psycopg2 import sql, DatabaseError

# Define connection parameters
params = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'mac240!',
    'port': '5432',
    'dbname': 'dev_money_app'
}

conn = psycopg2.connect(**params)

conn.autocommit = True

cur = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS test (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
)
"""

try:

    cur.execute(create_table_sql)
    print("Table creation attempted.")
except DatabaseError as e:
    print("Error in creating table:", e)


cur.close()
conn.close()
