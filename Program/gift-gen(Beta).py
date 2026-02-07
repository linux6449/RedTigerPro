import random
import os
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

now = datetime.now()
curtime = now.strftime("%H:%M")
author = "fullsafe."
path = os.getcwd()

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def back():
    input(f"{curtime} Press Enter to go back...")
    clearcmd()

def options():
    clearcmd()
    print(Fore.RED + """
            ██████╗ ███████╗██████╗     ████████╗██╗ ██████╗ ███████╗██████╗     ██████╗ ██████╗  ██████╗ 
            ██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗
            ██████╔╝█████╗  ██║  ██║       ██║   ██║██║  ███╗█████╗  ██████╔╝    ██████╔╝██████╔╝██║   ██║
            ██╔══██╗██╔══╝  ██║  ██║       ██║   ██║██║   ██║██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║
            ██║  ██║███████╗██████╔╝       ██║   ██║╚██████╔╝███████╗██║  ██║    ██║     ██║  ██║╚██████╔╝
            ╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ """)

    print(Fore.RED + """
[1] Generators
[2] Exit
    """)

    USER_OPTION = input(f"[=] Select an option:  ")

    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        clearcmd()
        print("Exiting...")
        time.sleep(1)
        quit()
    else:
        print(f"[-] Unknown input: '{USER_OPTION}', Try again.")
        time.sleep(1)
        back()
        options()

def generators():
    clearcmd()
    print(Fore.RED + """
            ██████╗ ███████╗██████╗     ████████╗██╗ ██████╗ ███████╗██████╗     ██████╗ ██████╗  ██████╗ 
            ██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗
            ██████╔╝█████╗  ██║  ██║       ██║   ██║██║  ███╗█████╗  ██████╔╝    ██████╔╝██████╔╝██║   ██║
            ██╔══██╗██╔══╝  ██║  ██║       ██║   ██║██║   ██║██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║
            ██║  ██║███████╗██████╔╝       ██║   ██║╚██████╔╝███████╗██║  ██║    ██║     ██║  ██║╚██████╔╝
            ╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
          """)

    print(Fore.RED + """
[1] Amazon Gift Card Generator
[2] Netflix Gift Card Generator
[3] Roblox Gift Card Generator
[4] Apple Gift Card Generator
[5] Steam Gift Card Generator
[6] Google Play Gift Card Generator
[7] Spotify Gift Card Generator
[8] Back to Main Menu
    """)

    USER_OPTION = input("[=] Select an option:  ")

    if USER_OPTION == "1":
        clearcmd()
        amazon()
    elif USER_OPTION == "2":
        clearcmd()
        netflix()
    elif USER_OPTION == "3":
        clearcmd()
        roblox()
    elif USER_OPTION == "4":
        clearcmd()
        apple()
    elif USER_OPTION == "5":
        clearcmd()
        steam()
    elif USER_OPTION == "6":
        clearcmd()
        googleplay()
    elif USER_OPTION == "7":
        clearcmd()
        spotify()
    elif USER_OPTION == "8":
        clearcmd()
        options()
    else:
        print(f"[-] Unknown input: '{USER_OPTION}', Try again.")
        time.sleep(1)
        back()
        generators()

def amazon():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
     █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nAmazon gift card format: {Fore.RED}XXXX-XXXXXX-XXXX\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "amazon.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            firstrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            secondrandom = ''.join(random.choice(CHARACTERS) for _ in range(6))
            thirdrandom = ''.join(random.choice(CHARACTERS) for _ in range(5))
            
            result = f"{firstrandom}-{secondrandom}-{thirdrandom}"
            file.write(result + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def netflix():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
    ███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                            
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nNetflix gift card format: {Fore.RED}XXXX-XXXXXX-XXXX\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "netflix.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            firstrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            secondrandom = ''.join(random.choice(CHARACTERS) for _ in range(6))
            thirdrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            
            result = f"{firstrandom}-{secondrandom}-{thirdrandom}"
            file.write(result + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def roblox():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
    ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║       
    ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                       
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nRoblox gift card format: {Fore.RED}XXXX-XXXX-XXXX-XXXX\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "roblox.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            firstrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            secondrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            thirdrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            fourthrandom = ''.join(random.choice(CHARACTERS) for _ in range(4))
            
            result = f"{firstrandom}-{secondrandom}-{thirdrandom}-{fourthrandom}"
            file.write(result + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def apple():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
     █████╗ ██████╗ ██████╗ ██╗     ███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██████╔╝██████╔╝██║     █████╗      ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║     ██║     ███████╗███████╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                   
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nApple gift card format: {Fore.RED}XXXXXXXXXXXXXXXX (16 characters)\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "apple.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            code = ''.join(random.choice(CHARACTERS) for _ in range(16))
            file.write(code + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def steam():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
    ███████╗████████╗███████╗ █████╗ ███╗   ███╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗   ██║   █████╗  ███████║██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                               
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nSteam gift card format: {Fore.RED}XXXXX-XXXXX-XXXXX\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "steam.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            firstpart = ''.join(random.choice(CHARACTERS) for _ in range(5))
            secondpart = ''.join(random.choice(CHARACTERS) for _ in range(5))
            thirdpart = ''.join(random.choice(CHARACTERS) for _ in range(5))
            
            result = f"{firstpart}-{secondpart}-{thirdpart}"
            file.write(result + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def googleplay():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗      ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗█████╗██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝╚════╝██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██║         ╚██████╔╝███████╗██║ ╚████║                                                                                                                                                                                                                                                                                                                                                                                                                                       
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nGoogle Play gift card format: {Fore.RED}XXXXXXXXXXXXXXXX (16 characters)\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "googleplay.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            code = ''.join(random.choice(CHARACTERS) for _ in range(16))
            file.write(code + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def spotify():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    """)
    print(f"""{Fore.RED}     [ Created by: {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Preparing settings...")
    time.sleep(1)
    print(f"\nSpotify gift card format: {Fore.RED}XXXX-XXXX-XXXX-XXXX-XXXX-XX (24 characters)\n")
    
    while True:
        try:
            howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many codes do you want to generate:  ")
            howmany = int(howmany)
            if howmany > 0:
                break
            else:
                print(f"{Fore.RED}[-] Enter a positive number!")
        except ValueError:
            print(f"{Fore.RED}[-] Enter a valid number!")

    output_dir = os.path.join(path, "3-Input", "Generated")
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, "spotify.txt")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating...")
    
    with open(file_path, "w+", encoding="utf-8") as file:
        for i in range(howmany):
            part1 = ''.join(random.choice(CHARACTERS) for _ in range(4))
            part2 = ''.join(random.choice(CHARACTERS) for _ in range(4))
            part3 = ''.join(random.choice(CHARACTERS) for _ in range(4))
            part4 = ''.join(random.choice(CHARACTERS) for _ in range(4))
            part5 = ''.join(random.choice(CHARACTERS) for _ in range(4))
            part6 = ''.join(random.choice(CHARACTERS) for _ in range(2))
            
            result = f"{part1}-{part2}-{part3}-{part4}-{part5}-{part6}"
            file.write(result + "\n")
            
            if (i + 1) % 100 == 0:
                print(f"{Fore.RED}[*] {i + 1}/{howmany} codes generated...")
    
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} gift cards")
    print(f"{Fore.RED}[+] Saved: {file_path}")
    
    back()
    clearcmd()
    generators()

def main():
    try:
        clearcmd()
        print(f"\n{Fore.RED}Press Enter to continue...")
        input()
        options()
    except KeyboardInterrupt:
        print(f"\n{curtime} CTRL + C detected, exiting...")
        time.sleep(1)
        quit()

if __name__ == "__main__":
    output_dir = os.path.join(path, "3-Input", "Generated")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"{Fore.RED}[+] Created: {output_dir}")
        time.sleep(1)
    
    main()