'''
DESAFIO 09:
Construa um programa que calcule: Você tem uma lista de preços de produto, todos
os produtos acima de R$5.000 vão ser reajustados em 5% e todos abaixo de R$5.000
vão ser reajustados em 10%, como ficam os preços dos produtos?
'''

# Função para moeda do Brasil


def lista_precos_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Definir as variáveis
lista_precos = [3200, 6890, 4500, 5500, 1798]
reajuste1 = 0.05
reajuste2 = 0.10
corte_faixa = 5000
lista_precos_reajustados = []

# Passo 2 - Calcular os preços reajustados
for preco in lista_precos:
    if preco <= corte_faixa:
        novo_preco = preco + (preco * reajuste1)
    else:
        novo_preco = preco + (preco * reajuste2)

# Passo 3 - Adicionar o novo preço à lista de preços reajustados
    lista_precos_reajustados.append(novo_preco)

# Passo 4 - Exibir os preços reajustados
print("Lista de preços reajustados:")
for preco in lista_precos_reajustados:
    print(lista_precos_formatado(preco))
