'''
DESAFIO 07:
Construa um programa que calcule: Calcule o contrário agora, quanto tempo demora
para esse funcionário chegar em um salário de 10.000,00 reais?
'''

# Função para moeda do Brasil


def salario_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Declaração de variáveis
salario = 2000
aumento = 0.10
tempo_servico = 0
meta = 10000

# Passo 2 - Calcular o salário em 10 anos
while salario < meta:
    tempo_servico += 1
    salario = salario + (salario * aumento)

# Passo 3 - Exibir o salário final e tempo de serviço
print(f"Salário final: {salario_formatado(salario)}")
print(f"Tempo de serviço: {tempo_servico} anos")
