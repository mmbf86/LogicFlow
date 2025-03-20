'''
DESAFIO 06:
Construa um programa que calcule: Qual seria o salário de um funcionário após 10
anos se todo ano ele ganhasse 10% de aumento, salário inicial de R$2.000,00?
'''

# Função para moeda do Brasil


def salario_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Calcular o salário final
salario_inicial = 2000
aumento = 0.10
tempo_servico = 10

# Passo 2 - Calcular o salário final
for i in range(tempo_servico):
    salario_inicial += salario_inicial * aumento

# Passo 3 - Exibir o salário final
print(f"Salário final: {salario_formatado(salario_inicial)}")
