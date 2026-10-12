import pymysql

def get_connection():
    return pymysql.connect(
        host='db',
        user='root',
        password='admin',
        database='zoo',
    )