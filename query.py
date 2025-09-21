import psycopg2
from config import load_config

def get_vendors():
    """Retrieve data from the vendors table"""
    config = load_config()
    try:
        with psycopg2.connect(**config)as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                rows = cur.fetchall() # fetchone()
                print("The number of parts:", cur.rowcount)

                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError) as error:
        print(error)


def iter_row(cursor, size=10):
    """An iterator that uses fetchmany to keep memory usage down"""
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """Retrieve data from the vendors table (joins)"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON parts.part_id = vendor_parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name;
                """)
                for row in iter_row(cur, 10):
                    print(row)
    except (psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    # get_vendors()
    get_part_vendors()
    print("Operation done successfully")
                
