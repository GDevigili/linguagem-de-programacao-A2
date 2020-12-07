from UFCMaster import UFCMaster
um = UFCMaster()

#####################QUESTÕES UFC#####################

# Qual lado ganhou mais?
Player = UFCMaster()
print(Player.vitoriasPorLado())
# Quem ganhou mais lutas?
Player = UFCMaster()
print(Player.vitoriasPorLutador())
# Quais partidas duraram menos?

# Qual peso que tem mais integrantes?
Player = UFCMaster()
print(Player.contagemCategoria())
# Quem ganhou mais vezes seguidas?

# Quem perdeu mais vezes seguidas?

# Quantos rounds durou a maior luta?

# Qual o máximo de ataques significativos dados pelo lado azul por minuto? (B_avg_SIG_STR_landed)

# Quantas derrubadas o lado azul fez a cada 15 minutos? (B_avg_TD_landed)

# Quantas vitórias por decisão unânime o lado azul teve? (B_win_by_Decision_Unanimous)

# Quantos anos tem o lutador mais velho? (R_age)

# Quantas lutas aconteceram em uma arena vazia? (empty_arena)

# Quantas vitórias o lado vermelho teve a mais que o azul?
# vitoriasAzul = self.df[self.df["Winner"] == "Blue"]["Winner"].value_counts().head(1)[0]
# vitoriasVermelhas = self.df[self.df["Winner"] == "Red"]["Winner"].value_counts().head(1)[0]
# print(vitoriasVermelhas - vitoriasAzul)