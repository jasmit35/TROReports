"""
std_dbconn
"""
from dotenv import load_dotenv
import os
import psycopg2


def get_database_connection(environment):
    load_dotenv("local/etc/db_secrets.env")
    host_name = os.getenv(f"{environment}_DB_HOST".upper())
    database = os.getenv(f"{environment}_DB_DATABASE".upper())
    username = os.getenv(f"{environment}_DB_USERNAME".upper())
    password = os.getenv(f"{environment}_DB_PASSWORD".upper())
    connection = pg_get_connection(host=host_name, database=database, username=username, password=password)
    connection.autocommit = True
    return connection


def pg_get_connection(host="localhost", database="pgdb", username="jeff", password="password"):
    connstr = f"dbname={database} user={username} password={password} host={host} port=5432"
    connection = None

    try:
        connection = psycopg2.connect(connstr)
    except Exception as e:
        raise


    return connection