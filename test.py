import random as rand
import os
from colorama import Fore , Style
from faker import Faker

os.system('cls')

def dashes():
    string1 = []
    for i in range(0,len(str1)):
        if (i == 2 or i==4 or i==-1):
            string1 += str1[i]
        else:
            string1 += "_"
    return string1  

def update(select):
    for i in range (0,len(str1)):
        if select==str1[i]:
            string1[i] = str1[i]
    return string1

def print_life():
    if life >= 4:
        print(Fore.BLUE+"Life Count: ",life)
        print(Style.RESET_ALL,end="")
    else:
        print(Fore.RED+"Life Count: ",life)
        print(Style.RESET_ALL,end="")

while True:
    fake = Faker()
    random_words = [fake.word() for _ in range(5)]
    life = 7
    str1 = rand.choice(random_words)
    string1 = dashes()
    print(string1)

    while True:
        os.system('cls')
        print_life()
        print(string1)
        while (True):
            select = input("Enter a letter: ").lower()
            if (len(select) == 1):
                break
            else:
                print(Fore.RED+"Enter a single chrarcter !")
                print(Style.RESET_ALL)
        if select in str1:
            string1 = update(select)
            print(string1)
        if select not in str1:
            life -= 1
            if life == 0:
                print(str1)
                print(Fore.RED+"You lost !")
                print(Style.RESET_ALL,end="")
                break
        if "_" not in string1:
            print(Fore.GREEN+"You Won !")
            print(Style.RESET_ALL,end="")
            break
    x = input("You want to play again (Yes/No): ")
    if x.upper() == "YES":
        life = 7
    else:
        break

