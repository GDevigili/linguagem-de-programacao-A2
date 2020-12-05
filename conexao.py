import pyodbc

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


cursor.execute("elect * from sys.databases") 
for r in cursor.fetchall():
    print(r)
    
connection.close()