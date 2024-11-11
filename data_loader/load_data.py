import redis
import psycopg2

from datetime import datetime
from utilities.queries import QUERIES


# Connection with Redis
r = redis.Redis(host='redis',port=6379,db=0)

# Connection with PostgreSQL using psycopg2
conn_string = "host='host.docker.internal' dbname='datadb' user='tsandil' password='stratocaster'"
postgres_conn = psycopg2.connect(conn_string)
cur = postgres_conn.cursor()

def load_data():
    keys = r.keys('crypto_data:*')
    if keys:
        for key in keys:
            try:
                _price = r.get(key)
                price = _price.decode('utf-8')
                timestamp = datetime.now()
                query = f"{QUERIES['insert_to_crypto']}".format(
                    schema_name = 'crypto',
                    table_name = 'crypto_prices'
                )
                cur.execute(query,(price,timestamp))
                postgres_conn.commit()
                print(f"Inserted data: {price} at {timestamp}")

                # Remove the key after inserting into PostgreSQL
                r.delete(key) 
                
            except Exception as e:
                print(f"Data Failed to load : {e}")
    else:
        print("No data found in Redis.")


if __name__ == '__main__':
    load_data()
