import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db_params

def insert_data():
    sql = """INSERT INTO vendor(name, contact_phone) VALUES(%s, %s)"""
    data = ('Scania', '+46789836444')

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Data inserted successfully")
        cur.close()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    insert_data()
