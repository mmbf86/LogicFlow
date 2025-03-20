'''
DESAFIO 03:
Construa um programa que calcule: Qual deve ser o bônus de um funcionário? Se ele
vendeu mais de 1.000 unidades, o bônus tem que ser de R$250, caso contrário, o
bônus tem que ser R$50
'''

# Função para moeda do Brasil


def bonus_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Definir as variáveis
vendas_funcionario = 1250
meta_vendas = 1000

# Passo 2 - Calcular o bônus e exibir o resultado
if vendas_funcionario >= meta_vendas:
    bonus = 250
else:
    bonus = 50

# Passo 3 - Exibir o bônus
print(f"Bônus de R$ {bonus_formatado(bonus)}")
