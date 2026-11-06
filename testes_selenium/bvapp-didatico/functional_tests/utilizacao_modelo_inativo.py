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

# O usuário com permissão para criar atas através de um modelo, tenta criar uma nova ata utilizando um Modelo de Ata com status "inativo".

# O sistema deve  barrar a utilização do Modelo de Ata Inativo, e exibir uma mensagem informando que não é possível utilizar o modelo de ata marcado como "inativo".