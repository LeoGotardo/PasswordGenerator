from alive_progress import alive_bar, config_handler
from alive_progress import *
import random as r
import Debug as d
import pyperclip
import os


def main():
    cls = os.system("cls")
    config_handler.set_global(length=50)
    tam = int(input(f"{d.Margin}Quantos digitos deve ter sua senha?\n"))
    num = input(f"{d.Margin}Deve ter numeros? S/N\n")
    letter = input(f"{d.Margin}Deve ter letras? S/N\n")
    symb = input(f"{d.Margin}Deve ter simbolos? S/N\n")
    maius = input(f"{d.Margin}Deve ter letras maiusculas? S/N\n")
    print(d.Margin)

    let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    may = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sim = ['!','@','#','$','%','¨','&','*','(',')','+','=','|','<','>',':',';','?']
    numb = ['0','1','2','3','4','5','6','7','8','9']
    password = []
    fin = []

    if num.lower() == "s":
        for i in range(len(numb)):
            fin.append(numb[i])
    if letter.lower() == "s":
        for i in range(len(let)):
            fin.append(let[i])
    if symb.lower() == "s":
        for i in range(len(sim)):
            fin.append(sim[i])
    if maius.lower() == "s":
        for i in range(len(may)):
            fin.append(may[i])
    with alive_bar(tam, title="Generating your password...") as bar:
        for i in range(tam):
            act = r.choice(fin)
            password.append(act)
            d.Green
            bar()
    fin_pass = ''.join(password)

    cls
    
    pyperclip.copy(fin_pass)
    print(F"{d.Margin}Sua senha copiada a sua clipbord.{d.Margin}")

main()
