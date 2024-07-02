# 💸 Sistema Bancário em Python
Bem-vindo ao Sistema Bancário em Python! Este projeto é uma aplicação que simula operações bancárias básicas. Ele permite o cadastro de clientes, a criação de contas correntes, e a realização de transações como depósitos, saques e visualização de extratos.
## :rocket: Funcionalidades
-**Cadastrar Clientes:** Crie novos clientes com informações pessoais;  
-**Criação de Contas:** Abra contas para clientes existentes;  
-**Depósitos:** Realize depósitos na conta;  
-**Saques:** Efetue saques respeitando os limites definidos;  
-**Extratos:** Visualize o histórico de transações de uma conta.
## :technologist: Tecnologias Utilizadas  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
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
git clone https://github.com/Francisquasedev/Sistema_bancario_version3.git
```
2. Execute o script principal:
```
python sistema_bancario_v3.py
```
3. Siga as instruções no menu para utilizar as funcionalidades do sistema.
## :heavy_plus_sign: Contribuição  
Contribuições são sempre bem-vindas! Para contribuir:  
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (**`git checkout -b feature/nova-feature`**).
3. Commit suas mudanças (**`git commit -m 'Adiciona nova feature'`**).
4. Faça um push para a branch (**`git push origin feature/nova-feature`**).
5. Abra um Pull Request.
## :page_facing_up: Licença  
Este projeto está licenciado sob a  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
## :globe_with_meridians: Contato  
Francis Monteles - [LinkedIn](www.linkedin.com/in/francis-monteles) - quasedev@protonmail.com 
