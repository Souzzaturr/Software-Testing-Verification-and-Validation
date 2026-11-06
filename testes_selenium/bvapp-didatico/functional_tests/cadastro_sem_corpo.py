'''
RF-25292: Criação de Modelos de Ata

Objetivo: Permitir que o usuário possa cadastrar novos Modelos de Ata.

Requisitos: 
- RF001

Ator:
- Usuário
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O usuário acessa a página de Modelos de Atas e aperta no botão "+ Adicionar Modelo de Ata" e começa a editar o documento, adicionando os seguintes dados de entrada:

# Definição de onde ficarão os campos obrigatórios
# Definiçao de onde ficarão as Tags
# Definião de onde ficarão as Variaveis

# Porém, o usuário não define o corpo do Modelo de Ata

# Após o usuário apertar em cadastrar, sem ter definido um corpo para o Modelo de Ata, o sistema deve barrar o envio, e exibir uma mensagem dizendo que o campo Corpo do Modelo de Ata é obrigatório.