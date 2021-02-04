import forca
import adivinhacao

def escolha_jogo():
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************")

    print("(1) Forca (2)Adivinhação")

    jogo = int(input("Digite o jogo desejado: "))

    if(jogo == 1):
        print("Jogando forca.")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação.")
        adivinhacao.jogar()
    else:
        print("Jogo inválido!")

if(__name__ == "__main__"):
    escolha_jogo()