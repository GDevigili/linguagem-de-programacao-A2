import Conexao as con
import pandas as pd

class CovidAeroporto():
    """Constroi um método para responder cada pergunta feita."""
    
    def __init__(self):
        """
        Inicia a conexao com o banco de dados, importa os dados e encerra a conexao.

        Returns
        -------
        None.

        """
        self.conexao = con.Conexao()
        self.df = self.conexao.getCovidImpactDataFrame()
        self.conexao.fecharConexao()    
           
    def maiorBaselinePorPais(self):
        """
        Responde a pergunta 'Em quais países o número de voos aumentou comparado com o período?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Country' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["Country"]
        maiorNumeroVoos = max(aux_df["Country"])
        
        return aux_df[aux_df["Country"] == maiorNumeroVoos]
    
    def menorBaselinePorPais(self):
        """
        Responde a pergunta 'Em quais países o número de voos diminuiu comparado com o período?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Country' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["Country"]
        menorNumeroVoos = min(aux_df["Country"])
        
        return aux_df[aux_df["Country"] == menorNumeroVoos]
    
    def maiorBaselinePorEstado(self):
        """
        Responde a pergunta 'Em quais estados o número de voos aumentou comparado com o período?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'State' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["State"]
        maiorNumeroVoos = max(aux_df["State"])
        
        return aux_df[aux_df["State"] == maiorNumeroVoos]
    
    def menorBaselinePorEstado(self):
        """
        Responde a pergunta 'Em quais estados o número de voos diminuiu comparado com o período?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'State' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["State"]
        menorNumeroVoos = min(aux_df["State"])
        
        return aux_df[aux_df["State"] == menorNumeroVoos]
    
    def maiorBaselinePorCidade(self):
        """
        Responde as perguntas 'Em que cidades dos EUA o número de voos aumentou?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'City' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["City"]
        maiorNumeroVoos = max(aux_df["City"])
        
        return aux_df[aux_df["City"] == maiorNumeroVoos]
    
    def menorBaselinePorCidade(self):
        """
        Responde as perguntas 'Em que cidades dos EUA o número de voos diminuiu?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'City' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["City"]
        menorNumeroVoos = min(aux_df["City"])
        
        return aux_df[aux_df["City"] == menorNumeroVoos]
    
    
    def maiorNumeroVoosPorDia(self):
        """
        Responde as perguntas 'Qual dia teve o maior número de voos internacionalmente?'.

        Returns
        -------
        aux_df : DataFrame
            DataFrame com colunas 'Date' e 'QtdVoos'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        maiorNumeroVoos = max(aux_df["QtdVoos"])
        
        return aux_df[aux_df["QtdVoos"] == maiorNumeroVoos]
        # aux_df = pd.DataFrame(self.df["Date"].value_counts())
        # aux_df.columns = ["QtdVoos"]
        # return aux_df
        # return aux_df.sort_values(by = aux_df["QtdVoos"], ascending = True)
        # a linha acima estava retornando um key error
    
    def menorNumeroVoosPorDia(self):
        """
        Responde as perguntas 'Qual dia teve o menor número de voos internacionalmente?'.

        Returns
        -------
        aux_df : DataFrame
            DataFrame com colunas 'Date' e 'QtdVoos'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        menorNumeroVoos = min(aux_df["QtdVoos"])
        
        return aux_df[aux_df["QtdVoos"] == menorNumeroVoos]

    def maiorBaselinePorDia(self):
        """
        Responde a pergunta 'Qual foi o dia com a maior baseline média?' 

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Date' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["PercentOfBaseline"]
        maiorNumeroVoos = max(aux_df["PercentOfBaseline"])
        
        return aux_df[aux_df["PercentOfBaseline"] == maiorNumeroVoos]

    def menorBaselinePorDia(self):
        """
        Responde a pergunta 'Qual foi o dia com a menor baseline média?' 

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Date' e 'PercentOfBaseLine'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["PercentOfBaseline"]
        menorNumeroVoos = min(aux_df["PercentOfBaseline"])
        
        return aux_df[aux_df["PercentOfBaseline"] == menorNumeroVoos]

a = CovidAeroporto()

# Qual dia teve o maior número de voos internacionalmente?
print(a.maiorNumeroVoosPorDia())
# Qual dia teve o menor número de voos internacionalmente?
print(a.menorNumeroVoosPorDia())
#Qual foi o dia com a maior baseline média?
print(a.maiorBaselinePorDia())
#Qual foi o dia com a menor baseline média?
print(a.menorBaselinePorDia())
#Qual cidade teve a maior porcentagem de baseline?
print(a.maiorBaselinePorCidade())
#Qual estado teve a maior porcentagem de baseline?
print(a.maiorBaselinePorEstado())
#Qual país teve a maior porcentagem de baseline?
print(a.maiorBaselinePorPais())
#Qual cidade teve a menor porcentagem de baseline?
print(a.menorBaselinePorCidade())
#Qual estado teve a menor porcentagem de baseline?
print(a.menorBaselinePorEstado())
#Qual país teve a menor porcentagem de baseline?
print(a.menorBaselinePorPais())




   

