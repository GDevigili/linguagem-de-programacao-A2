from CovidAeroporto import CovidAeroporto

#####################QUESTÕES AEROPORTO#####################
Pilot = CovidAeroporto()

# Em quais países o número de voos aumentou comparado com o período?
if Pilot.baselinesPorPais() >= Pilot.baselinePorDia():
    print(Pilot.Country)
# Em que cidades dos EUA o número de voos aumentou?
if Pilot.baselinePorCidade >= Pilot.baselinePorDia():
   print(Pilot.City)  
# Em que cidades dos EUA o número de voos diminuiu?
if Pilot.baselinePorCidade <= Pilot.baselinePorDia():
   print(Pilot.City)  
# Qual dia teve o maior número de voos internacionalmente?
print(Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = False))
# Qual dia teve o menor número de voos internacionalmente?
print(Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = True))
# Comparando o dia com mais voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = False) >= Pilot.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")    
# Comparando o dia com menos voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if Pilot.numeroVoosPorDia().values_sort(by = ["Date"], ascending = True) >= Pilot.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")
