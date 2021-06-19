Instruções para configuração do módulo pymongo no Python

1. Pré-requisito: Python instalado na estação de trabalho (preferencialmente acima da versão 3.8)

2. Em algum console de linha de comando (Prompt, Powershell, zsh, bash), executar a instalação do "redis":
    python -m pip install redis

3. Recomendo a utilização de alguma extensão para navegação em objetos Redis, como a extensão Redis ou Azure Cache do Visual Studio Code. Outros softwares de gerenciamento Redis podem ser encontrados na Internet, como nos exemplos do site a seguir: https://awesomeopensource.com/projects/redis-client

Instruções para configuração/criação do Redis na Azure

1. Sobre os recursos em Cloud, recomenda-se a criação de um "Azure Cache for Redis", com as configurações básicas (mais baratas), e aguardar a finalização de configuração do mesmo.
    a. Lembrar de, quando concluído o provisionamento, habilitar a conexão via non-SSL, para não requerer instalação/configuração de certificado

2. Capturar o host/URL de conexão e também as chaves (keys) de conexão e substituir nos arquivos .py

Dos exercícios e validações de entendimento:

1. Utilizar os métodos de insert-one (set) para criar um objeto no Cache com chave e valor
2. Tentar capturar este objeto pelo método get da biblioteca passando a chave do mesmo
3. Veja que não é possível buscar pelo conteúdo do agregado ou algum atributo dentro do mesmo. É sempre pela chave.
