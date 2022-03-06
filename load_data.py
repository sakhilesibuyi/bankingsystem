import __future__
import sqlite3
from queries import sql_queries
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def insertMultipleRecords(recordList,query):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        logging.info("Connected to SQLite")

        
        cursor.executemany(query, recordList)
        sqliteConnection.commit()
        logging.info("Total %s Records inserted successfully into SqliteDb_developers table", cursor.rowcount )
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        logging.error("Failed to insert multiple records into sqlite table %s", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("SQLite connection is closed")



if __name__ == "__main__":
    query=sql_queries
    for qry in sql_queries:
        logging.info("query %s",qry['query'])
        insertMultipleRecords(qry['data'],qry['query'])
    
