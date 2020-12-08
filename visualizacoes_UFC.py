import Conexao as con
import pandas as pd
import seaborn as sns


conexao = con.Conexao()
df = conexao.getUfcDataFrame()
conexao.fecharConexao() 


vencedor = df.groupby("Winner")["Winner"].count().sort_values(ascending = False) 
df_vencedor = pd.DataFrame({"winner": vencedor.index, "count": vencedor.values}) 
sns.barplot(x = "winner", y = "count", data = df_vencedor).set_title("Distribuição dos ganhadores por lado")

categoria = df.groupby('weight_class')['weight_class'].count().sort_values(ascending = False)[0:5]
df_categoria = pd.DataFrame({'weight_class': categoria.index, "count": categoria.values}) 
sns.barplot(x = 'weight_class', y = "count", data = df_categoria).set_title("Distribuição dos lutadores por categoria")

sns.histplot(df["no_of_rounds"]).set_title('Distribuição das lutas por rounds')

vermelhos = df[df["Winner"] == "Red"]["R_fighter"]
azuis = df[df["Winner"] == "Blue"]["B_fighter"]
df_vermelho = pd.DataFrame({"count": vermelhos.index, "winner": vermelhos.values})
df_azul = pd.DataFrame({"count": azuis.index, "winner": azuis.values}) 
winners = pd.concat([df_azul,df_vermelho])
sns.barplot(x = "winner", y = "count", data = winners.head(5)).set_title("Cinco jogadores com menos vitórias")

df_vermelhos = pd.DataFrame({"count": vermelhos.index, "winner": vermelhos.values})
df_azuis = pd.DataFrame({"count": azuis.index, "winner": azuis.values}) 
winners = pd.concat([df_azuis,df_vermelhos])[-5:]
sns.barplot(x = "winner", y = "count", data = winners.head(5)).set_title("Quatro jogadores com mais vitórias")