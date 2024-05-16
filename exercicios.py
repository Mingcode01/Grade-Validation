#Gabarito da prova:
gab = {
    "1": 'D',
    "2": 'A',
    "3": 'C',
    "4": 'B',
    "5": 'A',
    "6": 'D',
    "7": 'C',
    "8": 'C',
    "9": 'A',
    "10": 'B'}

lis_resp  = []
cont = 0
acertos = 0
erros = 0

for qst in range(0, 10):
  lis_resp.append(input(f"Digite a resposta da questão número {qst + 1}: "))

for num, resp in gab.items():
  if lis_resp[cont] == resp:
    acertos += 1
    print(f"0{num} - {resp} > A sua resposta foi: {lis_resp[cont]} > ✓")
    cont += 1
  else:
    print(f"0{num} - {resp} > A sua resposta foi: {lis_resp[cont]} > X")
    cont += 1
    erros += 1
print(f"A sua nota é {10*(acertos/10)}")
