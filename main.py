import os
import random
import sys
import time

from colorama import init, Fore
from rich.console import Console

init()


def welcome():
    msg = "Welcome to cnsl"
    for i in range(len(msg)):
        time.sleep(0.2)
        color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
        message = color + msg[:i + 1]
        sys.stdout.write('\r' + message + Fore.RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    msg2 = "Press enter to continue"
    for i in range(len(msg2)):
        time.sleep(0.2)
        color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
        message = color + msg2[:i + 1]
        sys.stdout.write('\r' + message)
        sys.stdout.flush()
        time.sleep(0.1)
    input("\n" + Fore.RESET)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


welcome()


def hack(site):
    console = Console()

    data = ["[cyan][italic]Passwords 🔑", "[cyan][italic]Secret Data 🔐", "[cyan][italic]Files 📁"]
    with console.status("[bold green]Fetching data...") as status:
        while data:
            num = data.pop(0)
            time.sleep(1)
            console.log(f"[green]Hacking https://{site}[/green] {num}")

        console.log(f'[bold][red]Done!')


while True:
    cmd = input(f"{Fore.LIGHTCYAN_EX}cnsl~ {Fore.LIGHTGREEN_EX}$ {Fore.RESET}")
    if "hack" in cmd:
        hack(str(cmd[5:]))
    elif "ip" in cmd:
        hack(str(cmd[3:]))


