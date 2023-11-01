# Random Password Generator - Documentation

## Introduction

This Python program generates a random password of a desired length, comprising symbols, letters (both lowercase and uppercase), and numbers.

## How to Use

1. Run the program in your preferred Python environment.
2. Enter the desired length of the password when prompted by the application.
3. Choose whether the password should contain numbers, letters (both lowercase and uppercase), and symbols by answering with 'S' (Yes) or 'N' (No).
4. The program will then generate a random password based on your choices and display it on the screen.

## Program Logic

- The program consists of a single function:

### 1. `main()`

- This is the main function that generates the random password based on user preferences.
- It starts by clearing the screen (for better user experience).
- The function takes input from the user regarding the password's length and whether it should contain numbers, letters, symbols, and uppercase letters.
- Lists containing characters for each category (e.g., `let` for lowercase letters) are initialized.
- Based on the user's choices, characters from the corresponding lists are appended to the `fin` list, which represents the characters to be used to generate the password.
- A loop then generates the password by randomly selecting characters from the `fin` list and appending them to the `password` list.
- Finally, the password is joined into a single string and displayed on the screen.

## Example Usage

```
Quantos digitos deve ter sua senha?
10
Deve ter numeros? S/N
S
Deve ter letras? S/N
S
Deve ter simbulos? S/N
S
Deve ter letras maiusculas? S/N
S
Sua senha é: X7n8P>#i@h
```

## Note

- The program demonstrates a simple random password generator based on user preferences for password complexity.
- It is important to note that the program relies on the `random` module in Python, which is not cryptographically secure. For generating passwords for security-critical applications, it is recommended to use the `secrets` module, which provides cryptographically secure random numbers suitable for generating passwords. Additionally, a more robust password policy and input validation can be implemented for a real-world application.