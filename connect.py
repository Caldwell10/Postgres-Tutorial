import psycopg2
from config import load_config

def connect(config):
    """ Connect to the Postgres database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn: # create new database session
            print("Connected to the PostgreSQL server")
            return conn
    except (psycopg2.DatabaseError) as error:
        print(error)
    

if __name__ == '__main__':
    config = load_config()
    connect(config)


