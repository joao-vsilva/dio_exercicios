###################################################################################################################

def deposito():
    global valor, saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return valor, saldo, extrato

#==================================================================================================================

def saque(): # Falta ver a questão do armazenamento da conta
    global valor, excedeu_limite, excedeu_saldo, excedeu_saques, conta_corrente[clientes[cpf][cpf]]["conta"], limite, numero_saques, LIMITE_SAQUES, extrato

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = conta_corrente[clientes[cpf][cpf]]["conta"] > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        conta_corrente[clientes[cpf][cpf]]["conta"] -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return valor, excedeu_limite, excedeu_saldo, excedeu_saques,conta_corrente[clientes[cpf][cpf]]["conta"], limite, numero_saques, LIMITE_SAQUES, extrato

#==================================================================================================================

def extrato_conta():
    global extrato, saldo

    print("\n" + " EXTRATO ".center(52, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {conta_corrente[clientes[cpf][cpf]]["conta"]:.2f}")
    print("=" * 52)

#==================================================================================================================

def cadastrar_usuario():
    global clientes, cpf, id_cliente
    print("\n" + " CADASTRO ".center(50, "=") + "\n")
    id_cliente += 1
    cpf = int(input("Digite o seu CPF (Sem pontos ou traços): "))
    senha = input("Crie uma senha para login: ")
    nome_completo = input("Digite o seu nome completo: ")
    dia_nascimento = input("Digite o dia que nasceu: ")
    mes_nascimento = input("Digite o mês que nasceu: ")
    ano_nascimento = input("Digite o ano que nasceu: ")
    logradouro_endereco = input("Digite o seu logradouro: ")
    bairro_endereco = input("Digite o seu bairro: ")
    cidade_endereco = input("Digite o nome de sua cidade: ")
    sigla_estado_endereco = input("Digite a sigla do seu estado: ")
    clientes[cpf] = {
        "nome_completo": nome_completo, "cpf": cpf, "senha": senha, "data_nascimento": (dia_nascimento + "/" + mes_nascimento + "/" + ano_nascimento),
              "endereco": {"logradouro": logradouro_endereco, "bairro": bairro_endereco, "cidade": cidade_endereco, "sigla_estado": sigla_estado_endereco}}
    print("\n" + "=" * 50 + "\n")
    return clientes


#==================================================================================================================

def cadastrar_conta_bancaria():
    global conta_corrente
    id_conta_bancaria = id_conta_funcao()
    print("\n" + " CADASTRO CONTA ".center(50, "=") + "\n")
    conta_corrente[clientes[cpf]["cpf"]] = {"agencia": "0001", "id_conta": id_conta_bancaria, "conta": saldo}
    print(f"'{id_conta_bancaria}' é o ID de sua conta")
    return conta_corrente 

#==================================================================================================================

def criar_conta_extra(cpf):
    chave_nova_conta = f"{object(cpf)} + {i+1}"
    conta_corrente[cpf] = conta_corrente.get(conta, []) + [conta_extra[chave_nova_conta]] # TERMINAR
    return conta_corrente

#==================================================================================================================

def id_conta_funcao():
    global id_conta
    id_conta += 1
    return id_conta

#==================================================================================================================

conta = 0
clientes = {}
conta_corrente = {}
conta_extra = {}
limite = 500
extrato = ""
numero_saques = 0
id_cliente = 0
id_conta = 0
LIMITE_SAQUES = 3
i = 0

#==================================================================================================================

menu2 =f"""
{" MENU ".center(52, "=")}

[c] Casdastro
[l] Login
[q] Sair

=> """

menu3 = f"""Deseja criar uma nova conta corrente?
[s] SIM
[n] NÃO

=> """

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#==================================================================================================================

while True:

    opcao2 = input(menu2).lower()

    if opcao2 == "c":
        cadastrar_usuario()
        cadastrar_conta_bancaria()
    elif opcao2 == "l":
        while True:
            print("\n" + " LOGIN ".center(52, "=") + "\n")
            login = input("Digite o seu 'CPF': ")
            senha = input("Digite a sua senha: ")
            if login == clientes[login]["cpf"] and senha == clientes[login]["senha"]:

                while True:

                    pergunta_contra_extra = input(menu3).lower()

                    if pergunta_contra_extra == "n":
                        break

                    elif pergunta_contra_extra == "s":
                        criar_conta_extra(login)
                        break

                while True:

                    opcao = input(menu).lower()

                    if opcao == "d":
                        deposito()

                    elif opcao == "s":
                        saque()

                    elif opcao == "e":
                        extrato_conta()

                    elif opcao == "q":
                        break

                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.")

            else:
                print("Login incorreto")

    elif opcao2 == "q":
        break
