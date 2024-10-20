import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

# Below is the database connection, importing the information from the config.py file to keep the private user details separate.
def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx

# The below runs a select query in the DB and returns the results. Created this as a function to be reused when getting
# the whole list of monsters and just a singular one.
def select_query(query):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor(dictionary=True)
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

# The below runs a delete query in the DB, similarly to above, created a function that could be reused and called later.
def delete_query(query):
    db_connection = None

    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute(query)
        db_connection.commit()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

# Below gets all monsters from the database, runs the select_query function above.
def get_all_monster_records():
    query = """SELECT * FROM halloween_monster"""
    return select_query(query)

# Below is for a single monster with and ID input, runs the select_query function from above
def get_monster_record(id):
    query = """SELECT * FROM halloween_monster WHERE monster_id = {}""".format(id)
    result = select_query(query)
    return result[0]

#Below is to delete a monster by ID, it runs the delete_query function from above
def delete_monster_by_id(id):
    query = """DELETE FROM halloween_monster WHERE monster_id = {}""".format(id)
    delete_query(query)
    return {"msg" : f"You deleted record: {id}"}

# Below is the create monster query, it uses %s to represent values that will be input by the user later. It allows Python values to be translated to
# SQL values, such as None to NULL, and makes sure the data translates properly.
def create_monster_records(post_data):
    query = """INSERT INTO halloween_monster (monster_name, country_id, 
    weakness, favourite_food, identifying_features, url)
    VALUES (%s, %s, %s, %s, %s, %s)"""

    db_connection = None

    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute(query, tuple(post_data.values()))
        id = cur.lastrowid
        db_connection.commit()
        result = get_monster_record(id)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

if __name__ == "__main__":
    print(get_all_monster_records())
