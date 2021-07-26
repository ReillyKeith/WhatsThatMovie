import psycopg2
import csv


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
        conn.autocommit = True

        cursor = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to DB: {error}\n"
              f"DB-Details\n"
              f"Host: {db_host}\n"
              f"User: {db_user}\n"
              f"Port: {db_port}\n"
              f"Pass: {db_pass}\n")
    return cursor


def create_tables(conn):
    """
    This function will create the tables
    that are required to stored the imdb data
    """
    try:
        conn.execute(open("sql_code/createTable_name_basic.sql", "r").read())
        conn.execute(open("sql_code/createTable_principals.sql", "r").read())
        conn.execute(open("sql_code/createTable_ratings.sql", "r").read())
        conn.execute(open("sql_code/createTable_title_basic.sql", "r").read())
        conn.execute(open("sql_code/createTable_title_crew.sql", "r").read())
        conn.execute(open("sql_code/createTable_title_episode.sql", "r").read())
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"There was an issue: {error}"
              f"\nPlease make sure sql tables are recreated")


def populate_tables(conn):
    """
    This function will store all the
    data from the txt files inside the tables
    :return:
    """
    with open("datasets/name.basics.txt", newline='') as file:
        line_reader = csv.reader(file, delimiter='\t')
        for line in line_reader:
            primary_name = line[1].replace("'", ' ')
            insert_sql = 'INSERT INTO public.imdb_name_basic("nconst", "primaryName", "birthYear", "deathYear", ' \
                         '"primaryProfession", "knownForTitles")' \
                         f"VALUES ('{line[0].strip()}', '{primary_name}', '{line[2].strip()}'," \
                         f" '{line[3].strip()}', '{line[4].strip()}', '{line[5].strip()}'); "
            conn.execute(insert_sql)

    with open("datasets/title.basics.txt", newline='') as file:
        line_reader = csv.reader(file, delimiter='\t')
        for line in line_reader:
            insert_sql = 'INSERT INTO public.imdb_title_basic(tconst, "titleType", "primaryTitle", ' \
                         '"originalTitle", "isAdult", "startYear", "endYear", "runtimeMinutes", genres) ' \
                         f"VALUES ('{line[0].strip()}', '{line[1].strip()}', " \
                         f"'{line[2].strip()}','{line[3].strip()}', " \
                         f"'{line[4].strip()}', '{line[5].strip()}) " \
                         f"'{line[6].strip()}', '{line[7].strip()}) " \
                         f"'{line[8].strip()}'); "
            conn.execute(insert_sql)
