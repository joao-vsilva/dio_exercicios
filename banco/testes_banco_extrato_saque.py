resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))

i = 0
limite_saque_diario = 3
MAX_VALOR_SAQUE = 500
extrato_saque = ["","",""]
conta = 100

while True:
    if resposta == 2:
        if limite_saque_diario > 0 and limite_saque_diario <= 3:
            valor_saque = float(input("Diga quanto quer sacar: "))
            if valor_saque > 0 and valor_saque <= 500:
                if valor_saque <= conta:
                    print("O dinheiro está saindo na boca do caixa...")
                    j = i + 1
                    extrato_saque[i] = (f"{j}º saque R$ {valor_saque:.2f}")
                    i += 1
                    limite_saque_diario -= 1
                    resposta = int(input("""
      [1] para depositar
      [2] para fazer um saque
      [3] para ver o extrato
      [0] para sair
      : """))
    else:
        break

                    
for i in range(3):
    print(extrato_saque[i])