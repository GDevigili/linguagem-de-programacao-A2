import pyodbc
server = 'Server=tcp:fgv-db-server.database.windows.net'
database = 'fgv-db'
username = 'student'
password = '@dsInf123'   
driver= '{ODBC Driver 17 for SQL Server}'

connection = pyodbc.connect("DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database+";UID="+username+";PWD="+password)

#connection = "Server=tcp:fgv-db-server.database.windows.net,1433;Initial Catalog=fgv-db;Persist Security Info=False;User ID=student;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"


with pyodbc.connect(connection) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

