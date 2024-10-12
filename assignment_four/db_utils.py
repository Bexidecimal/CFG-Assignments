import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx


def select_query(query):
    """Runs a SELECT query and returns results"""
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


def delete_query(query):
    """Runs a DELETE query"""
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


# Below gets all monsters
def get_all_monster_records():
    """Select all monster records from the DB"""
    query = """SELECT * FROM halloween_monster"""
    return select_query(query)


# Below is for a single monster
def get_monster_record(id):
    """Select single monster record from the DB based on the ID input"""
    query = """SELECT * FROM halloween_monster WHERE monster_id = {}""".format(id)
    result = select_query(query)
    return result[0]


def delete_monster_by_id(id):
    query = """DELETE FROM halloween_monster WHERE monster_id = {}""".format(id)
    delete_query(query)
    return {"msg" : f"You deleted record: {id}"}


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
