Instruções para configuração do módulo pymongo no Python

1. Pré-requisito: Python instalado na estação de trabalho (sugestão de ser acima da versão 3.8)

2. Em algum console de linha de comando (Prompt, Powershell, zsh, bash), executar a instalação do "pymongo":
    python -m pip install pymongo

Instruções para criação/configuração dos recursos em nuvem Azure

1. Criar CosmosDB e selecionar a API MongoDB
2. Definir o resource group (caso não tenha criado previamente)
3. Definir o nome único e a região de provisionamento
4. Após a criação, acessar o "quick start" para auxiliar a codificação na linguagem de programação preferida (no nosso exercício estamos utilizando Python)

Exercícios e validações:
1. Utilizar o método de "insert_one" para criar objetos no banco, verificando o atributo "_id" que será criado automaticamente
2. Utilizar o método de "find_one" para buscar objetos pelo valor dos atributos contindos dentro do agregado

