# Sistema Bancário Versão 3.0
from datetime import date, datetime
from abc import ABC, abstractmethod

# Variáveis globais
#saldo = 0
#saque = 0
#qtd_dep = 0
#qtd_saque = 0
#num_cpf = 0
num_conta = 0
clientes = []
contas = []
pessoas = []
AGENCIA = "0001"

class PessoaFisica:
    """Representa uma pessoa física com CPF, nome e data de nascimento."""
    
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        """
        Inicializa uma nova instância de PessoaFisica.

        Args:
            cpf (str): O CPF da pessoa.
            nome (str): O nome da pessoa.
            data_nascimento (date): A data de nascimento da pessoa.
        """
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Cliente:
    """Representa um cliente com endereço e pessoa associada."""

    def __init__(self, endereco: str, pessoa: PessoaFisica):
        """
        Inicializa uma nova instância de Cliente.

        Args:
            endereço (str): O endereço do cliente.
            pessoa (PessoaFisica): A pessoa física associada ao cliente.
        """
        self.endereco = endereco
        self.contas = []
        self.pessoa = pessoa
        
    def adicionar_conta(self, conta):
        """
        Adiciona uma conta ao cliente.

        Args:
            conta (Conta): A conta a ser adicionada.
        """
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta do cliente.

        Args:
            conta (Conta): A conta onde a transação será realizada.
            transacao (Transacao): A transação a ser realizada.
        """
        conta.realizar_transacao(transacao)

class Conta:
    """Representa uma conta bancária genérica."""

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente):
        """
        Inicializa uma nova instância de Conta.

        Args:
            saldo (float): O saldo inicial da conta.
            numero (int): O número da conta.
            agencia (str): A agência da conta.
            cliente (Cliente): O cliente associado a conta.
        """
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self) -> float:
        """
        Retorna o saldo atual da conta.

        Returns:
            float: O saldo da conta.
        """
        return self.saldo
    
    @staticmethod
    def nova_conta(cliente: Cliente, numero: int) -> 'Conta':
        """
        Cria uma nova conta para um cliente.

        Args:
            cliente (Cliente): O cliente para quem a conta será criada.
            numero (int): O número da conta.

        Returns:
            Conta: A nova conta criada.
        """
        return Conta(0.0, numero, AGENCIA, cliente)
    
    def sacar(self, valor: float) -> bool:
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        return True
    
    def depositar(self, valor: float) -> bool:
        """
        Realiza um depósito na conta.

        Args: 
            valor (float): O valor a ser depositado.

        Returns:
            bool: True se o depósito foi realizado com sucesso, False caso contrário.
        """
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True
    
class ContaCorrente(Conta):
    """Representa uma conta corrente com limite e limite de saques."""

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, limite: float, limite_saques: int):
        """
        Inicializa uma nova instância de ContaCorrente.

        Args:
            saldo (float): O saldo inicialda conta.
            numero (int): O número da conta.
            agencia (str): A agência da conta.
            cliente (Cliente): O cliente associado a conta.
            limite (float): O limite de créditoda conta.
            limite_saques (int): O limite de saques diários da conta.
        """
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    """Representa o histórico de transações de uma conta."""

    def __init__(self):
        """Inicializa umma nova instância de Historico."""
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico.

        Args:
            transacao (Transacao): A transacao a ser adicionada.
        """
        self.transacoes.append(transacao)
        

class Transacao(ABC):
    """Classe abstrata para representar uma transação bancária."""

    @abstractmethod
    def registrar(self, conta: Conta):
        """Registra a transção em uma conta."""
        pass

class Deposito(Transacao):
    """Representa uma transação de depósito."""

    def __init__(self, valor: float):
        """
        Inicializa uma nova instância de Deposito.

        Args:
            valor (float): O valor do depósito.
        """
        self.valor = valor

    def registrar(self, conta: Conta):
        """
        Registra a transação de depósito em uma conta.

        Args:
            conta (Conta): A conta onde o depósito será realizado.
        """
        conta.depositar(self.valor)

class Saque(Transacao):
    """Representa uma transação de saque."""

    def __init__(self, valor: float):
        """
        Inicializa uma nova instância de Saque.

        Args:
            valor (float): O valor do saque.
        """
        self.valor = valor

    def registrar(self, conta: Conta):
        """
        Registra a transação de saque em uma conta.

        Args:
            conta (Conta): A conta onde o sque será realizado.
        """
        conta.sacar(self.valor)


def criar_cliente():
    """
    Solicita informações do usuário e cria um novo cliente e pessoa física.

    Returns:
        tuple: Um objeto Cliente e um objeto PessoaFisica.
    """
    print("Você escolheu a opção Cadastrar Novo Cliente!")
    nome = input("Informe o seu nome: ")
    while True:
        dt_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
        try:
            data_nasc = datetime.strptime(dt_nascimento, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data de nascimento inválida. Por favor, insira novamente.")
    num_cpf = input("Informe o seu número de CPF (somente números): ")
    endereco = input("Informe o seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    pessoa = PessoaFisica(num_cpf, nome, data_nasc)
    cliente = Cliente(endereco, pessoa)

    return cliente, pessoa

def criar_conta(clientes):
    """
    Solicita informações do usuário e cria uma nova conta para um cliente existente.
    
    Args:
        clientes (list): A lista de clientes cadastrados.

    Returns:
        Conta: A nova conta criada, ou None se o cliente não foi encontrado.
    """
    print("Você escolheu a opção Criar Nova Conta: ")
    num_cpf = input("Informe um CPF já cadastrado: ")
    cliente = next((c for c in clientes if c.pessoa.cpf == num_cpf), None)
    if cliente:
        global num_conta 
        num_conta += 1
        conta = ContaCorrente(0, num_conta, AGENCIA, cliente, 1000, 3)
        cliente.adicionar_conta(conta)
        print("Conta criada com sucesso. Número da conta: ", num_conta,"\n")
        return conta
    else:
        print("Cliente não cadastrado. Por favor, criar cadastro primeiro! \n")
        return None

def realizar_deposito(conta):
    """
    Solicita informações do usuário e realiza um depósito em uma conta.

    Args:
        conta (Conta): Aconta onde o depósito será realizado.
    """
    print("Você escolheu a opção Depósito.")
    deposito = float(input("Informe o valor que será depositado: "))
    if deposito > 0:
        conta.depositar(deposito)
        print("Depósito realizado com sucesso!")
        print(f"Valor depositado: R$ {deposito:.2f}")
        print(f"Saldo: R$ {conta.saldo:.2f} \n")
    else:
        print("Valor informado é inválido. \n")

def realizar_saque(conta):
    """
    Solicita informações do usuário e realiza um saque de uma conta.

    Args:
        conta (Conta): A conta onde o sque será realizado.
    """
    print("Você escolheu a opção Saque.")
    saque = float(input("Informe o valor que deseja sacar: "))
    if conta.sacar(saque):
       print("Saque realizado com sucesso!")
       print(f"Valor do saque: R$ {saque:.2f}")
       print(f"Saldo: R$ {conta.saldo:.2f} \n")
    else:
        print("Operação não concluída. Verifique os limites ou saldo insuficiente. \n")

def ver_extrato(conta):
    """
    Exibe o extrato de uma conta.

    Args: 
        conta (Conta): A conta cujo extrato será exibido.
    """
    print("Você escolheu a opção Extrato.")
    print("Visualizar Extrato")
    if conta.historico.transacoes:
        for transacao in conta.historico.transacoes:
            print(type(transacao).__name__, transacao.valor)
        print(f"Saldo: R$ {conta.saldo:.2f} \n")
    else:
        print("Não foram realizadas movimentações na conta. \n")


# Loop principal do menu
while True:
    # Exibindo o menu inicial e solicitando uma escolha  do usuário
    menu_inicial = int(input('''Escolha uma das opções:
    [1] Depósito
    [2] Saque 
    [3] Extrato
    [4] Cadastrar Clientes
    [5] Criar Conta
    [0] Sair
    ''')) 

    # ÍNICIO DEPÓSITO
    if menu_inicial == 1:
        num_conta = int(input("Informe  o número da conta: "))
        conta = next((conta for conta in contas if conta.numero == num_conta), None)
        if conta:
            realizar_deposito(conta)
        else:
            print("Conta não encontrada.")
    # FIM DEPÓSITO
            
    # ÍNICIO SAQUE
    elif menu_inicial == 2:
        num_conta = int(input("Informe o número da conta: "))
        conta = next((conta for conta in contas if conta.numero == num_conta), None)
        if conta:
            realizar_saque(conta)
        else:
            print("Conta não encontrada.")
    # FIM SAQUE

    # ÍNICIO EXTRATO
    elif menu_inicial == 3:
        num_conta = int(input("Informe o número da conta: "))
        conta = next((conta for conta in contas if conta.numero == num_conta), None)
        if conta:
            ver_extrato(conta)
        else: print("Conta não encontrada.")
    # FIM EXTRATO

    # ÍNICIO CADASTRAR CLIENTE
    elif menu_inicial == 4:
        cliente, pessoa = criar_cliente()
        clientes.append(cliente)
        pessoas.append(pessoa)
        print(f"Cliente {pessoa.nome} cadastrado com sucesso!")
    # FIM CADASTRO CLIENTE

    # ÍNICIO CRIAR CLIENTE
    elif menu_inicial == 5:
        conta = criar_conta(clientes)
        if conta:
            contas.append(conta)
    # FIM CRIAR CLIENTE

    # SAIR 
    elif menu_inicial == 0:
        print("Você escolheu a opção Sair.")
        print("Obrigado por usar este sistema. Até mais!!!")
        break

    else: 
 
        print("Opção inválida. Tente novamente.")