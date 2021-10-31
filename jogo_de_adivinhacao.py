import random
def jogo_adivinha():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    print("Qual nivel dificuldade desejado ")
    print("(1)Facil (2) medio (3)Dificil")
    nivel = int(input("Nivel escolhido ? "))
    if (nivel == 1):
        total_de_tentativas =20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada,total_de_tentativas))

        chute_str = input("Digite o seu numero: ")
        print("Você digitou: ",chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("VocÊ deve digitar um numero de 1 a 100:")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if(acertou):
            print("PARABENS VOCÊ ACERTOU e fez: {}  ".format(pontos))
            break
        else:
            print("EROUUUU")
            if(maior):
                print("seu numero foi maior que o numero secreto")
                if(rodada == total_de_tentativas):
                    print("O numero secreto era {}. Sua pontuação foi:".format(numero_secreto,pontos_perdidos))
            elif(menor):
                print("menor que o numero secreto")
                if(rodada == total_de_tentativas):
                    print("O numero secreto era {}. Sua pontuação foi:".format(numero_secreto,pontos_perdidos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1
        total_de_tentativas = total_de_tentativas -1
    print("End of the game")
    if(__name__ == "__main__"):
        jogo_adivinha()