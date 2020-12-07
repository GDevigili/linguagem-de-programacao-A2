from UFCMaster import UFCMaster

#####################QUESTÕES UFC#####################
Player = UFCMaster()

# Qual lado ganhou mais?
print(Player.vitoriasPorLado())
# Quem ganhou mais lutas?
print(Player.vitoriasPorLutador())
# Quantas partidas duraram menos?
print(Player.menorLuta())
# Qual peso que tem mais integrantes?
print(Player.contagemCategoria())
# Quem ganhou mais vezes seguidas?
print(Player.vitoriasSeguidas())
# Quem perdeu mais vezes seguidas?
print(Player.derrotasSeguidas())
# Quantos rounds durou a maior luta?
print(Player.maiorLuta())
# Quantas lutas tiveram um número mínimo de rounds?
print(Player.menorLuta())
# Qual o máximo de ataques significativos dados por minuto? 
print(Player.ataquesSignificativos())
# Quantas derrubadas o lado azul fez a cada 15 minutos? (B_avg_TD_landed)

# Quantas vitórias por decisão unânime o lado azul teve? (B_win_by_Decision_Unanimous)

# Quantos anos tem o lutador mais velho? 
print(Player.idades())
# Quantas lutas aconteceram em uma arena vazia? (empty_arena)
print(Player.Void())
# Quantas vitórias o lado vermelho teve a mais que o azul?
vitoriasAzul = Player.df[Player.df["Winner"] == "Blue"]["Winner"].value_counts().head(1)[0]
vitoriasVermelhas = Player.df[Player.df["Winner"] == "Red"]["Winner"].value_counts().head(1)[0]
print(vitoriasVermelhas - vitoriasAzul)