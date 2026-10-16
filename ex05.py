# leitura da quantidade de minutos
minutos_totais = int(input("Digite os minutos: "))

# calculo do minuto e das horas
horas = minutos_totais // 60
minutos_restantes = minutos_totais % 60

# resultado
print(f"{horas} hora(s) e {minutos_restantes} minuto(s)")