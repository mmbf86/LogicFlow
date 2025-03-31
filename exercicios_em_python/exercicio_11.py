# Faça um jogo de pedra, papel e tesoura. O jogo deve:
# - Solicitar a escolha do jogador
# - Gerar uma escolha aleatória para o computador
# - Exibir a escolha do jogador e do computador
# - Exibir o resultado do jogo (você venceu, você perdeu ou empate)
# - Perguntar se deseja jogar novamente
# - Encerrar o jogo caso a resposta seja não
# - Utilize a biblioteca random para gerar a escolha do computador


import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha: pedra, papel ou tesoura? ").lower()

    if jogador not in opcoes:
        print("Escolha inválida. Tente novamente!")
        continue

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
    if jogar_novamente != "sim":
        print("Obrigado por jogar! Até a próxima.")
        break
