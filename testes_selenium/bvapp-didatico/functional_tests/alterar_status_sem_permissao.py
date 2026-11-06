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

# O usuário sem permissão para alterar status de Modelos de Ata, solicita ao sistema a alteração de status de um modelo de ata específico

# O sistema deve barra a alteração de status e exibir uma mensagem dizendo que o usuário não possui permissão para alterar o status de um Modelo de Ata.