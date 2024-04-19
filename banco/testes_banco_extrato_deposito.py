import numpy as np

resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))

limite_saque_diario = 3
MAX_VALOR_SAQUE = 500
extrato_saque = ["","",""]
extrato_deposito = np.empty((100), dtype=object)
conta = 0
posicao = 0
contador = 0

while True:
    if resposta == 1:
        deposito = float(input("Informe quanto você depositar: "))
        if deposito > 0:
            ordem2 = contador + 1
            extrato_deposito[contador] = f"{ordem2}º depósito R$ {deposito:.2f}"
            contador += 1
            conta += deposito
            resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
    else:
        break

        

for i in range(contador):
    print(extrato_deposito[i])
