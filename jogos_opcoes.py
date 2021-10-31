import jogo_de_adivinhacao
import jogo_da_forca

print("*********************************")
print(" * Bem Vindo a Tela Inicial! * ")
print("*********************************")

print("(1)Forca (2) Adivinhação ")
jogo =int(input("qual o jogo?"))
if(jogo == 1):
    print("Jogo da Forca")
    jogo_da_forca.jogo_forca()
elif(jogo ==2):
    print("Jogo de Adivinhação")
    jogo_de_adivinhacao.jogo_adivinha()