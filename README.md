# 🤖 Automação de Cadastro de Produtos

Projeto desenvolvido em Python para automatizar a leitura de uma base de dados de produtos e realizar o cadastro individual de cada item em um sistema web. O objetivo é otimizar tarefas repetitivas de digitação manual, reduzindo o tempo de execução e prevenindo erros operacionais.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** — Linguagem principal do projeto.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** — Automação de comandos de mouse e teclado.
- **[Pandas](https://pandas.pydata.org/)** — Manipulação e leitura da base de dados (`produtos.csv`).
- **[openpyxl](https://openpyxl.readthedocs.io/)** — Suporte para leitura de planilhas.

---

## 📋 Pré-requisitos e Instalação

Antes de executar o projeto, certifique-se de ter o Python e o PyCharm (ou VS Code) instalados na sua máquina.

Em seguida, instale as dependências executando o comando abaixo no terminal do seu ambiente:

```bash
pip install pyautogui pandas openpyxl
```
---
## Como Configurar e Executar 

**1. Configurar Credenciais e Arquivos

1.Certifique-se de que o arquivo produtos.csv esteja localizado na raiz da pasta do projeto.
2.Abra o arquivo principal (main.py) e insira suas credenciais de acesso nas variáveis:

```bash
  email = "seu_email@dominio.com"
  senha = "sua_senha"
```
## 2. Ajuste de Coordenadas de Tela (Opcional)

Como o PyAutoGUI utiliza coordenadas absolutas de clique na tela (x e y), verifique se as posições coincidem com a resolução do seu monitor. Caso precise atualizar, utilize o arquivo auxiliar.py:

```bash
import pyautogui
import time

time.sleep(3)
print(pyautogui.position())  # Exibe a posição exata do cursor no terminal
```

## 3. Rodando o Script

No PyCharm ou no seu terminal, execute o comando:

```bash
Bash
python main.py
```

## Fluxo e Comportamento da Execução

 Ao iniciar o script, o computador executará as seguintes etapas de forma automática:

1. Abertura do Navegador: O script pressiona a tecla Windows, digita "chrome" e abre o navegador.

2. Navegação e Autenticação: Acessa a URL do sistema, preenche o e-mail e a senha, e realiza o login.

3. Leitura da Base de Dados: O Pandas lê a tabela produtos.csv linha por linha.

4. Preenchimento Automático do Formulário: Para cada produto cadastrado na tabela, o script:

 - Clica no primeiro campo (Código do Produto).
  
 - Preenche em sequência: Código, Marca, Tipo, Categoria, Preço Unitário, Custo e Observações.
  
 - Pressiona Enter para enviar o cadastro.
  
 - Executa a rolagem da página para o topo (pyautogui.scroll(5000)) e reinicia o processo para o próximo item.

## ⚠️ Atenção durante a execução:
Como o PyAutoGUI assume o controle do mouse e do teclado, não mexa no mouse ou no teclado enquanto o script estiver rodando. Para interromper a automação de emergência, mova o cursor rapidamente para o canto superior esquerdo da tela.
