'''
DESAFIO 10:
Construa um programa para:
- Calcular o salário dos funcionários com reajuste de 10% (a partir de uma lista de
salários)
- Calcular o custo total de salários que o RH vai ter q pagar
- Calcular a diferença em R$ entre o cenário anterior e o cenário atual
'''

# Função para moeda do Brasil


def salario_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Variáveis iniciais
lista_salarios_iniciais = [2000, 5000, 10000, 7000, 12000]
custo_total = sum(lista_salarios_iniciais)
reajuste = 0.10

# Passo 2 - Calcular Salários Reajustados


def calcular_salarios_reajustados(lista_salarios_iniciais, reajuste):
    lista_salarios_reajustados = []
    for salario in lista_salarios_iniciais:
        lista_salarios_reajustados.append(salario + (salario * reajuste))
    return lista_salarios_reajustados

# Passo 3 - Calcular novo custo total de salários


def calcular_custo_total(lista_salarios_reajustados):
    return sum(lista_salarios_reajustados)

# Passo 4 - Calcular a diferença do novo custo total para o custo anterior


def calcular_diferenca_custo(custo_total, custo_total_reajustado):
    return custo_total_reajustado - custo_total


# Passo 5 - Variáveis finais
salarios_reajustados = calcular_salarios_reajustados(
    lista_salarios_iniciais, reajuste)
custo_total_reajustado = calcular_custo_total(salarios_reajustados)
diferenca_custo = calcular_diferenca_custo(custo_total, custo_total_reajustado)

# Passo 6 - Exibir resultados
print(f"Salários Iniciais: {lista_salarios_iniciais}")
print(f"Salários Reajustados: {salarios_reajustados}")
print(f"Custo Total Anterior: {salario_formatado(custo_total)}")
print(f"Custo Total Reajustado: {salario_formatado(custo_total_reajustado)}")
print(f"Diferença de Custo: {salario_formatado(diferenca_custo)}")
