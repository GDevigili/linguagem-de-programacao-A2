from CovidAeroporto import CovidAeroporto
ca = CovidAeroporto()

#####################QUESTÕES AEROPORTO#####################

# Em quais países o número de voos aumentou comparado com o período?

# Em que cidades dos EUA o número de voos aumentou?

# Em que cidades dos EUA o número de voos diminuiu?

# Qual dia teve o maior número de voos internacionalmente?
Pilot = CovidAeroporto()
print(Pilot.maiorNumeroVoos())
# Qual dia teve o menor número de voos internacionalmente?
Pilot = CovidAeroporto()
print(Pilot.menorNumeroVoos())
# Comparando o dia com mais voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
Pilot = CovidAeroporto()
print(Pilot.baselinePorDia())
# Comparando o dia com menos voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?