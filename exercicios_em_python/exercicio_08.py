'''
DESAFIO 08:
Construa um programa que calcule: Tenho uma lista de preços de produtos, se
fizermos um reajuste de 5% a mais em todos os produtos, como ficam os preços dos
produtos?
'''

# Função para moeda do Brasil


def lista_precos_formatado(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Passo 1 - Definir as variáveis
lista_precos = [100, 50, 80, 30, 20]
reajuste = 0.05
lista_precos_reajustados = []

# Passo 2 - Calcular os preços reajustados
for preco in lista_precos:
    lista_precos_reajustados.append(preco + (preco * reajuste))

# Passo 3 - Exibir os preços reajustados
print("Lista de preços reajustados:")
for preco in lista_precos_reajustados:
    print(lista_precos_formatado(preco))
