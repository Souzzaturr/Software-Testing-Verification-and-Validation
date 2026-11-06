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

# O usuário tenta acessar a página, porém não possui permissão para acessar a página

# O sistema deve exibir apenas uma página em branco e exibir uma mensagem informando que aquela página é restrita apenas para usuários com permissão para acessar aquela página, e perguntando se o usuário deseja retornar para a página anterior.



# 🟡 [FLUXO ALTERNATIVO] - Usuário com permissão de acesso à página porém sem permição para adição
# ---------------------------------------------------------------

# O usuário acessa a página de Modelos de Ata e solicita a criação de um Modelo de Ata

# O sistema deve barra a solicitação e exibir uma mensagem informando que o usuário não possui permissão para criar um novo modelo de Ata.