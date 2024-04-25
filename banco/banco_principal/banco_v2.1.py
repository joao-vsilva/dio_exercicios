def cadastrar_conta_bancaria():
    global conta_corrente
    id_conta_bancaria = id_conta_funcao()
    print("\n" + " CADASTRO CONTA ".center(50, "=") + "\n")
    conta_corrente[clientes[cpf]["cpf"]] = {"agencia": "0001", "id_conta": id_conta_bancaria, "conta": {id_conta_bancaria}}
    print(f"'{id_conta_bancaria}' é o ID de sua conta")
    return conta_corrente

def id_conta_funcao():
    global id_conta
    id_conta += 1
    return id_conta

conta_corrente[clientes[1234]["cpf"]] = {"agencia": "0001", "id_conta": id_conta_bancaria, "conta": {id_conta_bancaria}}

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

clientes[1234] = {
        "nome_completo": "João Victor", "cpf": "1234", "data_nascimento": "10/10/2005",
              "endereco": {"logradouro": "Rua", "bairro": "Vila", "cidade": "Lagoa", "sigla_estado": "PE"}}