import random
import sys
import os
import pyfiglet
from colorama import Fore, Style

# Color definitions
all_colors = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.LIGHTCYAN_EX,
    Style.BRIGHT + Fore.LIGHTBLUE_EX,
    Style.BRIGHT + Fore.LIGHTCYAN_EX,
    Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
    Style.BRIGHT + Fore.LIGHTYELLOW_EX
]

ran = random.choice(all_colors)

def get_password_file_path():
    """Get the path for passwords.txt in the parent directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    return os.path.join(parent_dir, "passwords.txt")

def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    """Display the program banner"""
    clear_screen()
    print(ran, pyfiglet.figlet_format("\tWordList\n\tGenerator"))
    print(ran + "\t\tVersion 3.0\t\n\n")
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3)

def exit_program():
    """Exit the program"""
    sys.exit()

def generate_passwords():
    """Generate password wordlist"""
    victim_name = input(ran + "\nEnter victim's name: ")
    password_amount = input(ran + "\nEnter number of passwords to generate: ")
    
    try:
        password_amount = int(password_amount)
    except ValueError:
        print(ran + "\nError: Please enter a valid number!")
        return
    
    add_info = input(ran + "\nDo you want to add more information? [y/n]: ")
    
    password_file_path = get_password_file_path()
    
    if add_info.lower() == "y":
        phone_number = input(ran + "\nEnter specific short number: ")
        instagram_id = input(ran + "\nEnter Instagram username: ")
        birth_date = input(ran + "\nEnter date of birth or month: ")
        company = input(ran + "\nEnter company name: ")
        city = input(ran + "\nEnter city: ")
        country = input(ran + "\nEnter country: ")
        additional_info = input(ran + "\nEnter any additional information: ")
        
        print(ran + "\n\t\tGenerating passwords, please wait...")
        
        try:
            with open(password_file_path, "a+", encoding="utf-8") as file:
                # Write basic combinations
                file.write(victim_name + victim_name + "\n")
                file.write(birth_date + victim_name + "\n")
                file.write(victim_name + phone_number + "\n")
                file.write(victim_name + company + "\n")
                file.write(victim_name + additional_info + "\n")
                file.write(victim_name + city + "\n")
                file.write(city + birth_date + "\n")
                file.write(city + phone_number + "\n")
                file.write(additional_info + city + "\n")
                file.write(birth_date + country + "\n")
                file.write(birth_date + additional_info + "\n")
                file.write(instagram_id + additional_info + "\n")
                file.write(instagram_id + "\n")
                file.write(birth_date + "\n")
                
                # Generate random number combinations
                for i in range(password_amount):
                    random_num = random.randint(0, 99999)
                    random_str = str(random_num).zfill(5)
                    
                    # Victim name combinations
                    file.write(victim_name + random_str + "\n")
                    file.write(phone_number + random_str + "\n")
                    file.write(instagram_id + random_str + "\n")
                    file.write(birth_date + random_str + "\n")
                    file.write(company + random_str + "\n")
                    file.write(city + random_str + "\n")
                    file.write(country + random_str + "\n")
                    file.write(additional_info + random_str + "\n")
                    
                    # Reverse combinations
                    file.write(random_str + additional_info + "\n")
                    file.write(random_str + victim_name + "\n")
                    file.write(random_str + phone_number + "\n")
                    file.write(random_str + instagram_id + "\n")
                    file.write(random_str + birth_date + "\n")
                    file.write(random_str + company + "\n")
                    file.write(random_str + city + "\n")
                    file.write(random_str + country + "\n")
                    file.write(random_str + random_str + "\n")
                    
            print(ran + f"\nPasswords saved to: {password_file_path}")
            
        except Exception as e:
            print(ran + f"\nError saving file: {e}")
    
    else:
        print(ran + "\n\t\tGenerating passwords, please wait...")
        
        try:
            with open(password_file_path, "a+", encoding="utf-8") as file:
                file.write(victim_name + victim_name + "\n")
                
                for i in range(password_amount):
                    random_num = random.randint(1000, 9999)
                    random_str = str(random_num)
                    
                    file.write(victim_name + random_str + "\n")
                    file.write(random_str + random_str + "\n")
                    file.write(random_str + victim_name + "\n")
            
            print(ran + f"\nPasswords saved to: {password_file_path}")
            
        except Exception as e:
            print(ran + f"\nError saving file: {e}")

def view_passwords():
    """View generated passwords"""
    password_file_path = get_password_file_path()
    
    try:
        if not os.path.exists(password_file_path):
            print(ran + "\nNo password file found!")
            return
        
        with open(password_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        print(ran + "\n\t\tGenerated Passwords:\n")
        
        if content.strip():
            print(all_colors[2 % 6] + content)
        else:
            print(ran + "File is empty!")
            
    except Exception as e:
        print(ran + f"\nError reading file: {e}")

def main():
    """Main program loop"""
    display_banner()
    
    continue_program = "y"
    while continue_program.lower() in ["y", "yes"]:
        print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Generate Passwords\n\t\t[2] View Generated Passwords\n\t\t[3] Exit\n")
        
        choice = input(ran + "Enter your choice: ")
        
        if choice == "1":
            generate_passwords()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print(ran + "\n\tDon't forget to follow me! :-)\t\n")
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4)
            print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3)
            exit_program()
        else:
            print(ran + "\nInvalid option!")
        
        continue_program = input(ran + "\nDo you want to continue? [y/n]: ")
        
        if continue_program.lower() in ["y", "yes"]:
            clear_screen()
            display_banner()

if __name__ == "__main__":
    main()