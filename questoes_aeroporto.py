from CovidAeroporto import CovidAeroporto

#####################QUESTÕES AEROPORTO#####################
Pilot = CovidAeroporto()

# Em quais países o número de voos aumentou comparado com o período?

# Em que cidades dos EUA o número de voos aumentou?

# Em que cidades dos EUA o número de voos diminuiu?

# Qual dia teve o maior número de voos internacionalmente?
print(Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = False))
# Qual dia teve o menor número de voos internacionalmente?
print(Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = True))
# Comparando o dia com mais voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if Pilot.numeroVoosPorDia() >= Pilot.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")    
# Comparando o dia com menos voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if Pilot.numeroVoosPorDia() >= Pilot.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")
# Em quais países o número de voos aumentou comparado com o período de baseline?
print(Pilot.df)
if Pilot.baselinesPorPais() >= Pilot.baselinePorDia():
    print(Pilot.Country)
