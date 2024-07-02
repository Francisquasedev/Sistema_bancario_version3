# 💸 Sistema Bancário em Python
Bem-vindo ao Sistema Bancário em Python! Este projeto é uma aplicação que simula operações bancárias básicas. Ele permite o cadastro de clientes, a criação de contas correntes, e a realização de transações como depósitos, saques e visualização de extratos.
## :rocket: Funcionalidades
-**Cadastrar Clientes:** Crie novos clientes com informações pessoais;  
-**Criação de Contas:** Abra contas para clientes existentes;  
-**Depósitos:** Realize depósitos na conta;  
-**Saques:** Efetue saques respeitando os limites definidos;  
-**Extratos:** Visualize o histórico de transações de uma conta.
## :technologist: Tecnologias Utilizadas
* **Python 3.9+**
* **Paradigma de Orientação a Objetos**
* **PEP 257:** Documentação e Docstrings
## :memo: Estrutura do Projeto
### Classes Principais:
**`PessoaFisica`:**
Representa uma pessoa física com CPF, nome e data de nascimento.
**`Cliente`:**
Representa um cliente do banco.  
**`Conta`:**
Representa uma conta bancária.  
**`ContaCorrente`:**
Especialização de **`Conta`** com limite de saques.  
**`Historico`:**
Armazena o histórico de transações de uma conta.  
**`Transacao`:**
Classe abstrata para representar uma transação.  
**`Deposito`:**
Transação de depósito.  
**`Saque`:**
Transação de saque.  
### Funções Principais:  
`criar_cliente` Solicita informações do usuário e cria um novo cliente.  
`criar_conta` Cria uma nova conta para um cliente existente.  
`realizar_deposito` Realiza um depósito em uma conta.  
`realizar_saque` Realiza um saque de uma conta.  
`ver_extrato` Exibe o extrato de uma conta.
## :pencil2: Iniciando
### Pré-requisitos  
* Python 3.9 ou superior
### Instalação  
1. Clone o repositório:
```

```
## :heavy_plus_sign: Contribuição
## :page_facing_up: Licença
## :globe_with_meridians: Contato
