print("***************************")
print("****JOGO DE ADIVINHAÇÃO****")
print("***************************")
numero = 14
chute = input("Digite um número: ")
x = int(chute)
if x == numero:
    print("Você acertou!")
else:
    if x > numero:
        print("você errou! seu chute foi maior que o numero secreto")
    else:
        print("você errou! seu chute foi menor que o numero secreto")
print("********************************")
print("****USANDO O COMPARADOR ELIF****")
print("********************************")

number = 15
a = input("Informe um numero: ")
fmt = int(a)

acertou = fmt == number
maior = fmt>numero
menor = fmt<number
if(acertou):
    print("Você acertou!")
elif(maior):
    print("você errou! seu chute foi maior que o numero secreto")
elif(menor):
    print("você errou! seu chute foi menor que o numero secreto")
