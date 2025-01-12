import json

with open("fat.json", "r") as file:
    fatDiario = json.load(file)

fatValid = [dia["valor"] for dia in fatDiario if dia["valor"] > 0]

minFat = min(fatValid)
maxFat = max(fatValid)
medFat = sum(fatValid) / len(fatValid)
diaAcimaMed = sum(1 for valor in fatValid if valor > medFat)
print(f"O valor mínimo de faturamento é: {minFat}")
print(f"O valor máximo de faturamento é: {maxFat}")
print(f"O valor médio de faturamento é: {medFat}")
print(f"Há {diaAcimaMed} dias com faturamento acima da média")

#exemplo de json
# {"dia": 1, "valor": 22174.1664},
# {"dia": 2, "valor": 247853.1664},