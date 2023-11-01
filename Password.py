import os
import random as r

def main():
    cls = os.system("cls")
    tam = int(input(print(f"Quantos digitos deve ter sua senha?\n")))
    num = input(print(f"Deve ter numeros? S/N\n"))
    letter = input(print(f"Deve ter letras? S/N\n"))
    symb = input(print(f"Deve ter simbulos? S/N\n"))
    maius = input(print(f"Deve ter letras maiusculas? S/N\n"))

    let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    may = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numb = ['0','1','2','3','4','5','6','7','8','9']
    sim = ['ç','!','@','#','$','%','¨','&','*','(',')','+','=','|','<','>',':',';','?']
    fin = []
    password = []

    if num == "S" or num == "s":
        for i in range(len(numb)):
            fin.append(numb[i])
    if letter == "S" or letter == "s":
        for i in range(len(let)):
            fin.append(let[i])
    if symb == "S" or symb == "s":
        for i in range(len(sim)):
            fin.append(sim[i])
    if maius == "S" or maius == "s":
        for i in range(len(may)):
            fin.append(may[i])
    for i in range(tam):
        act = r.choice(fin)
        password.append(act)

    fin_pass = ''.join(password)

    cls
    print(F"Sua senha é: {fin_pass}")

main()
