import random as r
import pyperclip
import os


def main():
    cls = os.system("cls")
    tam = int(input(f"Quantos digitos deve ter sua senha?\n"))
    num = input(f"Deve ter numeros? S/N\n")
    letter = input(f"Deve ter letras? S/N\n")
    symb = input(f"Deve ter simbulos? S/N\n")
    maius = input(f"Deve ter letras maiusculas? S/N\n")

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
    for i in range(tam):
        act = r.choice(fin)
        password.append(act)

    fin_pass = ''.join(password)

    cls
    
    pyperclip.copy(fin_pass)
    print(F"Sua senha copiada a sua clipbord.")

main()
