import random

print("bienvenue à votre générateur de mot de passe")

chars = "abcdefghijklmnopqrstuvwxz!@#$%^&*()_+=-1234567890[]';:\|}{/.,?><"

number = int(input("saisissez la quantité de mot de passe à générer"))

length = int(input("saisissez la longueur du mot de passe"))

print("mot de passe :")

for i in range(number):
    passwords = ""
    for j in range(length):
        passwords +=random.choice(chars)
    print(passwords)

