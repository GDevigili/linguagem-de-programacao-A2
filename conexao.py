import pyodbc
import pandas as pd

server = "fgv-db-server.database.windows.net"
database = "fgv-db"
username = "student"
password = "@dsInf123"
driver = "{ODBC Driver 17 for SQL Server}"

connection = pyodbc.connect("DRIVER="+driver
                            + ";SERVER="+server
                            + ";PORT=1433;DATABASE="
                            + database+";UID="+username+";PWD="
                            + password)


cursor = connection.cursor()


#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute(""" 
        SELECT name, database_id, create_date  
        FROM sys.databases ;""") 
for r in cursor.fetchall():
    print(r)


# nomedb = u"fgv-db"

# SELECT = """\
#             SELECT *  
#             FROM ? ;"""
            
# cursor.execute(SELECT, (nomedb)) 
        
# for r in cursor.fetchall():
#     print(r)
    
    
# UPDATE_SQL3 = """
#     SELECT * FROM 
#     WHERE
#         STATION_ID = ?
# """

# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=local;DATABASE=DB;UID=me;PWD=pass')
# cursor = conn.cursor()

# cursor.execute(UPDATE_SQL3 %
#                            (name,
#                             title,
#                             active,
#                             id
#                             ))



    
# connection.close()