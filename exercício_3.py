import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

soma = 0
dias = 0
maior = 0
menor = 0
flag = True
for i in dados:
    if i['valor']>0:
        if flag == True:
            maior = i["valor"]
            menor = i["valor"]
            dias+=1
            soma += i["valor"]
            flag = False
        else:
            if i["valor"]>maior:
                maior = i["valor"]
            if i["valor"]<menor:
                menor = i["valor"] 
            dias+=1
            soma+=i['valor']

media = soma/dias
dias_maiores = 0
for i in dados:
    if i['valor']>media:
        dias_maiores+=1

print(f'O menor faturamento foi de {menor}')
print(f'O menor faturamento foi de {maior}')
print(f'O Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é {dias_maiores}')