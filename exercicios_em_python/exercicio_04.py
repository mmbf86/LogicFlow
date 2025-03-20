'''
DESAFIO 04:
Construa um programa que calcule: Qual deve ser o bônus de um funcionário? Se a
empresa bateu a meta de 10.000 vendas E se ele vendeu mais de 1.000 unidades, o
bônus tem que ser de R$250, caso contrário, o bônus tem que ser R$50
'''

# Função para moeda do Brasil


def bonus_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - declarar as variáveis
meta_empresa = 10000
meta_funcinario = 1000
vendas_empresa = 15000
vendas_funcionario = 1250

# Passo 2 - Calcular o bônus e exibir o resultado

if vendas_empresa >= meta_empresa and vendas_funcionario >= meta_funcinario:
    bonus = 250
else:
    bonus = 50

# Passo 3 - Exibir o bônus
print(f"Bônus de R$ {bonus_formatado(bonus)}")
