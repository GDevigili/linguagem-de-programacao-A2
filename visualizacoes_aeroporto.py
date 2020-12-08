import Conexao as con
import pandas as pd
import seaborn as sns
import matplotlib as plt

conexao = con.Conexao()
df = conexao.getCovidImpactDataFrame()
conexao.fecharConexao() 


sns.histplot(df['PercentOfBaseline']).set_title('Distribuição de PercentOfBaseline')


sns.scatterplot(x = df["Country"],
                y=df["PercentOfBaseline"], data = df).set_title("Relação entre países e PercentOfBaseline")
sns.set_style("dark") 


g = sns.scatterplot(x = df["City"],
               y=df["PercentOfBaseline"], data = df)
g.set_xticklabels(g.get_xticklabels(), rotation=20)
g.set_title("Relação entre cidades e PercentOfBaseline")

aux_df = pd.DataFrame(df["Date"].value_counts())
aux_df.columns = ["QtdVoos"]
sns.scatterplot(x = aux_df.index,
                y=aux_df["QtdVoos"], data = aux_df)

sns.scatterplot(x = df["Date"],
                y=df["PercentOfBaseline"], data = df)


