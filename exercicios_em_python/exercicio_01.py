'''
DESAFIO 01:
Construa um programa que calcule: Quanto devemos cobrar em um projeto de
programação se trabalhamos 8h por dia, demoramos 15 dias para fazer o projeto e
cobramos R$100/h?
'''

# Função para moeda do Brasil


def formatar_moeda(valor): return f"R$ {valor:,.2f}".replace(
    ",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Calcular as horas trabalhadas
horas_por_dia = 8
dias_totais = 15
horas_trabalho = horas_por_dia * dias_totais
print(f"Horas trabalhadas: {horas_trabalho}")

# Passo 2 - Calcular o custo total
custo_hora = 100
custo_total = horas_trabalho * custo_hora

# Passo 3 - Exibir o custo total
# Formatando o valor manualmente
custo_total_formatado = formatar_moeda(custo_total)
print(f"Custo total: {custo_total_formatado}")
