print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = int(input("Digite o seu número: "))

acertou = chute_str == numero_secreto
maior   = chute_str > numero_secreto
menor   = chute_str < numero_secreto

print("Você digitou ", chute_str)

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo!")