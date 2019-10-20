'''
Useage: 
'''
import sys
import os
import csv
project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_root)

import address_book_manage.online_wechat_process as owp
from config import configer

data_dir = os.path.join(project_root,configer['permanent']['data_dir'])
friends_path = os.path.join(data_dir, configer['permanent']['friends_list_csv'])
group_path = os.path.join(data_dir,configer['permanent']['group_list_csv'])
db_path = os.path.join(data_dir,'address_book.db')
#print(data_dir,friends_path,group_path)

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
def create_sqlite(db_file):
    """ create a database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


 
def main():
    #Init db
    #create_sqlite(db_path)
    pass
 
if __name__ == '__main__':
    main()
