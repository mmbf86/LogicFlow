'''
DESAFIO 02:
Construa um programa que calcule: Quanto custa encher o tanque de um carro que
tem 50 litros de capacidade, está com 20 litros de combustível atualmente e o custo
do combustível é de R$5,80/litro?
'''

# Passo 1 - Calcular a capacidade restante do tanque
max_tanque = 50
capacidade_preenchida = 20
capacidade_restante = max_tanque - capacidade_preenchida

# Passo 2 - Calcular o preço para encher o tanque
litro = 5.80
preco_encher = capacidade_restante * litro

# Passo 3 - Exibir o preço para encher o tanque
print("Preço para encher o tanque: R$ {:.2f}".format(preco_encher))
