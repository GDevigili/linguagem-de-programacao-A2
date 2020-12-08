import pyodbc
import pandas as pd
import sys

server = "fgv-db-server.database.windows.net"
database = "fgv-db"
username = "student"
password = "@dsInf123"
driver = "{ODBC Driver 17 for SQL Server}"
initialCatalog = "fgv-db";

class Conexao:
    """Constroi a conexao com o banco de dados a ser usado."""
    def __init__(self):
        """
        Inicia a conexao com o banco de dados.
        
        Returns
        -------
        None.
        
        """
        try:
            self.conexao = pyodbc.connect("DRIVER="+driver
                            + ";SERVER="+server
                            + ";Initial Catalog ="+initialCatalog
                            + ";PORT=1433;DATABASE="
                            + database+";UID="+username+";PWD="
                            + password)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '28000':
                ("LDAP Connection failed: check password")
                print("Usuário e/ou senha incorretos. Tente Novamente.")
            if sqlstate == '08001':
                print("Não foi possível iniciar a conexao com o banco de dados. Tente novamente.")
            sys.exit()
                
    # Isso vai para a respectiva classe
    def getUfcDataFrame(self):
        """
        Importa dados da tabela 'ufc.ufc_master' do banco 'fgv-db'.
        
        Returns
        -------
        DataFrame
            DataFrame correspondente a toda a tabela 'ufc.ufc_master'.
            
        """
        try:
            return pd.read_sql("SELECT * FROM ufc.ufc_master;", self.conexao)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '08S01':
                print("A conexao com o banco de dados foi perdida. Tente novamente.")
            sys.exit()
    
    def getCovidImpactDataFrame(self):
        """
        Importa dados da tabela 'covid.covid_impact_on_airport_traffic' do banco 'fgv-bd'.
        
        Returns
        -------
        DataFrame
            DataFrame correspondente a toda a tabela 'covid.covid_impact_on_airport_traffic'.
            
        """
        try:
            return pd.read_sql("SELECT * FROM covid.covid_impact_on_airport_traffic;", self.conexao)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '08S01':
                print("A conexao com o banco de dados foi perdida. Tente novamente.")
            sys.exit()
    
    def fecharConexao(self):
        """
        Encerra a conexao com o banco de dados.
        
        Returns
        -------
        None.
        
        """
        self.conexao.close()
        
c = Conexao()
c.getUfcDataFrame()