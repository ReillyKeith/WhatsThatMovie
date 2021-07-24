import psycopg2


def get_config_data(data):
    """
    This function will get all the data
    from the config file, which will then be
    used for DB connection
    :param data:
    :return: config values
    """
    db_host = data['pgAdmin']['pgAdmin_host']
    db_database = data['pgAdmin']['pgAdmin_database']
    db_user = data['pgAdmin']['pgAdmin_username']
    db_port = data['pgAdmin']['pgAdmin_port']
    db_pass = data['pgAdmin']['pgAdmin_pass']

    return db_host, db_database, db_user, db_port, db_pass


def connect_to_db(db_host, db_database,
                  db_user, db_port, db_pass):
    """
    This function will connect to the database,
    using the values setup in config file.
    :param db_host:
    :param db_database:
    :param db_user:
    :param db_port:
    :param db_pass:
    :return: cursor connection
    """
    try:
        conn = psycopg2.connect(
            host=f"{db_host}",
            database=f"{db_database}",
            user=f"{db_user}",
            port=f"{db_port}",
            password=f"{db_pass}")

        cursor = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to DB: {error}\n"
              f"DB-Details\n"
              f"Host: {db_host}\n"
              f"User: {db_user}\n"
              f"Port: {db_port}\n"
              f"Pass: {db_pass}\n")
    return cursor


def check_db_tables():
    """
    This function will check that the DB
    is setup and contain datasets.
    If not it will return false value
    :return:
    """
