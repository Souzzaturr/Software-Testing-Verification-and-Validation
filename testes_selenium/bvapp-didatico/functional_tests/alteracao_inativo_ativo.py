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

# O usuário com permissão para alterar o status de Modelos de Atas solicita a alteração do status de um modelo de ata específico com status "inativo" para "ativo".

# Então o sistema deve alterar o status do Modelo de Ata para "ativo".


# 🟡 [FLUXO ALTERNATIVO] Modelo já marcado como "inativo"
# ---------------------------------------------------------------

# Quando o sistema receber uma solicitação para alterar o status de um Modelo de Ata específico para o mesmo status que já está selecionado, o sistema deve barrar e exibir uma mensagem informando que o status do Modelo de Ata não pode ser alterado para o mesmo status.