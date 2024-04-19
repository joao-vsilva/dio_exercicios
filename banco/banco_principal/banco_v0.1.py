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
    if resposta == 0:
        break

    elif resposta == 1:
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
            
    elif resposta == 2:
        if limite_saque_diario > 0 and limite_saque_diario <= 3:
            valor_saque = float(input("Diga quanto quer sacar: "))
            if valor_saque > 0 and valor_saque <= 500:
                if valor_saque <= conta:
                    print("O dinheiro está saindo na boca do caixa...")
                    limite_saque_diario -= 1
                    ordem = posicao + 1
                    extrato_saque[posicao] = f"{ordem}º saque R$ {valor_saque:.2f}"
                    posicao += 1
                    resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
                else:
                    print("Saldo insuficiente para a operação\nSelecione uma das opções abaixo")
                    resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
            else:# Melhorar depois
                print("Cada saque é realizado com até R$ 500,00\n Selicione uma das opções abaixo")
                resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
        else:
            print("Você já alcançou o seu limite máximo de saques.\nVolte em outro dia útil")
            resposta = int(input("""
      [1] para depositar
      [3] para ver o extrato
      [0] para sair
      : """))
                
    elif resposta == 3: # Melhorar depois
        for i in range(3):
            print(extrato_saque[i])
        for i in range(contador):
            print(extrato_deposito[i])
        resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
