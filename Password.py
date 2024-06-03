from alive_progress import alive_bar, config_handler
import random as r
import Debug as d
import pyperclip
import os

class PasswordGenerator:
    """A class for generating random passwords based on specified criteria.
    
    Attributes:
        let (list of str): Lowercase letters.
        may (list of str): Uppercase letters.
        sim (list of str): Special characters.
        numb (list of str): Digits from 0 to 9.
    """
    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        """Initializes the PasswordGenerator with lists of characters used in password creation."""
        self.let = [chr(i) for i in range(97, 123)]  # a-z
        self.may = [chr(i) for i in range(65, 91)]  # A-Z
        self.sim = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '+', '=', '|', '<', '>', ':', ';', '?']
        self.numb = [str(i) for i in range(10)]  # 0-9
        print(f"""{d.Magenta}
______                                                 _    _____                                       _               
| ___ \                                               | |  |  __ \                                     | |              
| |_/ / __ _   ___   ___  __      __  ___    _ __   __| |  | |  \/   ___   _ __     ___   _ __   __ _  | |_   ___    _ __ 
|  __/ / _` | / __| / __| \ \ /\ / / / _ \  | '__| / _` |  | | __   / _ \ | '_ \   / _ \ | '__| / _` | | __| / _ \  | '__|
| |   | (_| | \__ \ \__ \  \ V  V / | (_) | | |   | (_| |  | |_\ \ |  __/ | | | | |  __/ | |   | (_| | | |_ | (_) | | |   
\_|    \__,_| |___/ |___/   \_/\_/   \___/  |_|    \__,_|   \____/  \___| |_| |_|  \___| |_|    \__,_|  \__| \___/  |_|   
                                                                                                          

""")
        include_numbers = input(f"{d.Margin}{d.LightMagenta}Must have numbers? (Y/N)\n")
        include_lowercase = input(f"{d.Margin}{d.LightMagenta}Must have letters? (Y/N)\n")
        include_symbols = input(f"{d.Margin}{d.LightMagenta}Must have symbols? (Y/N)\n")
        include_uppercase = input(f"{d.Margin}{d.LightMagenta}Must have uppercase? (Y/N)\n")
        size = input(f"{d.Margin}{d.Yellow}How much digits must have your password?\n")
        
        try:
            size = int(size)
        except:
            input(f"{d.Margin}The password size must be a number. (Press enything to try again){d.Margin}")
            PasswordGenerator()
        
        if include_numbers.lower() == 'y':
            include_numbers = True
        else:
            include_numbers = False
        if include_lowercase.lower() == 'y':
            include_lowercase = True
        else:
            include_lowercase = False
        if include_symbols.lower() == 'y':
            include_symbols = True
        else:
            include_symbols = False
        if include_uppercase.lower() == 'y':
            include_uppercase = True
        else:
            include_uppercase = False
            

        pyperclip.copy(self.generate_password(include_numbers, include_lowercase, include_symbols, include_uppercase, size))

    def generate_password(self, include_numbers: bool, include_lowercase: bool, include_symbols: bool, include_uppercase: bool, size: int) -> str:
        """Generates a random password based on the specified criteria.

        Args:
            include_numbers (bool): Whether to include numbers in the password.
            include_lowercase (bool): Whether to include lowercase letters in the password.
            include_symbols (bool): Whether to include symbols in the password.
            include_uppercase (bool): Whether to include uppercase letters in the password.
            size (int): The length of the password to generate.

        Returns:
            str: The generated password.
        """
        available_chars = []
        if include_numbers:
            available_chars.extend(self.numb)
        if include_lowercase:
            available_chars.extend(self.let)
        if include_symbols:
            available_chars.extend(self.sim)
        if include_uppercase:
            available_chars.extend(self.may)
            
        password = []

        with alive_bar(size, title="Generating your password...") as bar:
            for i in range(size):
                password.append(r.choice(available_chars))
                bar()
        return ''.join(password)
    

if __name__ == "__main__":
    passwordGenerator = PasswordGenerator()
