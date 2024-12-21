import sys
import os
import pyfiglet
from Logs import LogCollector
from colorama import Fore, init

os.environ['TERM'] = 'xterm-256color'

def title(title , color : Fore.MAGENTA):
    init()
    ascii_art = pyfiglet.figlet_format(title)
    print(color + ascii_art)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def body(menu1, menu2, menu3):
    while True:
        print(f"1 - {menu1}\n2 - {menu2}\n\n99 - {menu3}\n")
        choice = input("Choice : ")

        if choice == '99':
            sys.exit()
        elif choice == '1':
            blue_team_menu()
        elif choice == '2':
            red_team_menu()
        else:
            print("Invalid choice. Please try again.")


def blue_team_menu():
    while True:
        clear_screen()
        title("Blue Team",Fore.BLUE)
        print("1 - Log Collector")
        print("2 - Anomaly Detection")
        print("3 - Security Incident and Event Monitoring")
        print("4 - Threat intelligence integration")
        print("5 - Blocking Detected Threats\n")
        print("99 - Back")

        choice = input("Choice : ")

        if choice == '1':
            logCollector()
        elif choice == '2':
            anomaly_detection()
        elif choice == '99':
            main_menu()
        else:
            print("Invalid choice. Please try again.")


def red_team_menu():
    while True:
        clear_screen()
        title("Red Team",Fore.RED)
        print("1 - Vulnerability Assessment")
        print("2 - Exploitation")
        print("99 - Back")

        choice = input("Choice : ")

        if choice == '1':
            vulnerability_assessment()
        elif choice == '2':
            exploitation()
        elif choice == '99':
            main_menu()
        else:
            print("Invalid choice. Please try again.")


def logCollector():
    while True:
        clear_screen()
        log_type = input(Fore.MAGENTA + "Please choose log type (system/custom): ").strip().lower()

        if not log_type:
            print(Fore.RED + "Error: Log type cannot be empty. Please choose 'system' or 'custom'.\n")
            continue

        log_duration = input(Fore.MAGENTA + "Enter log duration (e.g., 1d for 1 day, 1h for 1 hour): ").strip()

        if not log_duration:
            print(Fore.RED + "Error: Log duration cannot be empty. Please enter a valid duration.\n")
            continue

        log_collector = LogCollector(log_type=log_type, duration=log_duration, log_file="logs_output.txt")
        log_collector.collect_logs()
        print(Fore.LIGHTCYAN_EX + "\nCollected Logs\n")
        input(Fore.BLUE + "Press Enter to return to the Blue Team menu...")
        blue_team_menu()
        break


def anomaly_detection():
    clear_screen()
    print(Fore.MAGENTA + "\nPerforming Anomaly Detection...")

    input("Press Enter to return to the Blue Team menu...")


def vulnerability_assessment():
    clear_screen()
    print(Fore.MAGENTA + "\nPerforming Vulnerability Assessment...")

    input("Press Enter to return to the Red Team menu...")


def exploitation():
    clear_screen()
    print(Fore.MAGENTA + "\nPerforming Exploitation...")

    input("Press Enter to return to the Red Team menu...")


def main_menu():
    title("Purple",Fore.MAGENTA)
    print(Fore.MAGENTA + "This application created for education is at your own risk.\n"
                         "\t\t\t\t\t\t\t\t\t\t\t Enskc05")
    body("Blue Team", "Red Team", "Exit")

main_menu()