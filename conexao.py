import pyodbc
import pandas as pd

server = "fgv-db-server.database.windows.net"
database = "fgv-db"
username = "student"
password = "@dsInf123"
driver = "{ODBC Driver 17 for SQL Server}"
initialCatalog = "fgv-db";

class Conexao:
    def __init__(self):
        self.conexao = pyodbc.connect("DRIVER="+driver
                            + ";SERVER="+server
                            + ";Initial Catalog ="+initialCatalog
                            + ";PORT=1433;DATABASE="
                            + database+";UID="+username+";PWD="
                            + password)
        
    def verificacaoConexao(self):
        cursor = self.conexao.cursor()
        
        
        #Informacoes sobre as tables (db, schema, nome, se é base table ou view)
        
        cursor.execute(""" 
              SELECT * FROM information_schema.TABLES 
                  WHERE TABLE_NAME = 'ufc_master' OR TABLE_NAME = 'covid_impact_on_airport_traffic'""") 
                
        for r in cursor.fetchall():
            print(r)
        
        print("\n\n\n")
        
        #Mostra todas as colunas da table 'covid_impact_on_airport_traffic'
        cursor.execute(""" 
              SELECT COLUMN_NAME 
                  FROM INFORMATION_SCHEMA.COLUMNS
                  WHERE TABLE_NAME = 'covid_impact_on_airport_traffic'""") 
                
        for r in cursor.fetchall():
            print(r)
            
        print("\n\n\n")
        
        #Mostra todas as colunas da table 'ufc_master'
        cursor.execute(""" 
              SELECT COLUMN_NAME 
                  FROM INFORMATION_SCHEMA.COLUMNS
                  WHERE TABLE_NAME = 'ufc_master'""") 
                
        for r in cursor.fetchall():
            print(r)
        
        print("\n\n\n")
        #Seleciona o primeiro registro de 'ufc_master'
        cursor.execute(""" 
              SELECT TOP(1) * FROM ufc.ufc_master;""") 
        for r in cursor.fetchall():
            print(r)
            
        print("\n\n\n")        
        #Seleciona o primeiro item de 'covid_impact_on_airport_traffic'          
        cursor.execute(""" 
              SELECT TOP(1) * 
              FROM covid.covid_impact_on_airport_traffic;
              """) 
             
              
        for r in cursor.fetchall():
            print(r)
    
    # Isso vai para a respectiva classe
    def getUfcDataFrame(self):
        return pd.read_sql("SELECT * FROM ufc.ufc_master;", self.conexao)
    
    def getCovidImpactDataFrame(self):
        return pd.read_sql("SELECT * FROM covid.covid_impact_on_airport_traffic;", self.conexao)
    
    def fecharConexao(self):
        self.conexao.close()
        