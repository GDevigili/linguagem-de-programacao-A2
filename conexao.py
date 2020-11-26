import pyodbc
server = 'Server=tcp:fgv-db-server.database.windows.net'
database = 'Initial Catalog=fgv-db'
username = 'student'
password = '<password>'   
driver= '{ODBC Driver 17 for SQL Server}'

connection = "Server=tcp:fgv-db-server.database.windows.net,1433;Initial Catalog=fgv-db;Persist Security Info=False;User ID=student;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"


'''
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
'''

with pyodbc.connect('DRIVER='+driver+';'+connection) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
