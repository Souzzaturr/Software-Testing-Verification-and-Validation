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

# O usuário acessa a página de Modelos de Atas e aperta no botão "+ Adicionar Modelo de Ata"
# E apertar em enviar, sem preencher nenhum campo

# Então o sistema deve barra o envio, e exibir uma mensagem dizendo que é necessário preencher todos os campos obrigatórios para poder enviar o Modelo de Ata para cadastro.