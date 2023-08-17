print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

SECRET_NUMBER = 42
TOTAL_ATTEMPS = 3
rodada = 1

for rodada in range(1, TOTAL_ATTEMPS + 1):
    print("Tentativa: {:n} de {:n}".format(rodada, TOTAL_ATTEMPS))
    chute_str = input("Digite seu numero: ")
    chute = int(chute_str)
    print("Você digitou: ", chute)

    correct = chute == SECRET_NUMBER
    isBigger = chute > SECRET_NUMBER
    isSmaller = chute < SECRET_NUMBER

    if (correct):
        print("Você acertou")
    elif (isBigger):
        print("Você errou! O numero secreto é menor")
    elif (isSmaller):
        print("Você errou! O numero secreto é maior")
    rodada = rodada + 1
