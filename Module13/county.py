#sample code to read the CSV file
import os as os
import csv 
import sqlite3
from sqlite3 import Error

def insertData(fileName, conn):    
    fullPath = os.path.join(os.path.dirname(__file__), fileName)
    #fullPath = fileName    

    with open(fullPath, 'r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            
            ## Add Rows to the Table
            create_county_record(conn, row)
    

def create_county_record(conn, county):
    sql = ''' INSERT INTO County(CountyName, Population, NumberOfHousehold)
            VALUES(?, ?, ?)'''
    c  = conn.cursor()
    c.execute(sql, county)
    return c.lastrowid

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None
def create_county_table(conn):
    try:
        sql_county_table = """ CREATE TABLE IF NOT EXISTS County (
                                        id integer PRIMARY KEY,
                                        CountyName text NOT NULL,
                                        Population INTEGER NOT NULL,
                                        NumberOfHousehold INTEGER NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_county_table)
    except Error as err:
        print(err)


def select_all_counties(conn):
    """Query all rows of county table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM County")

    rows = cur.fetchall()
    return rows # return the rows

if __name__ == '__main__':
    conn = create_connection("counties.db")
    with conn:
        create_county_table(conn)
        insertData('example.csv', conn)
        print(select_all_counties(conn))

