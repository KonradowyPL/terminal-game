from statusbar import displayNumber
from colorama import Fore
import sys

def end(player, reason):
        sys.stdout.write("\x1B[2J")
        sys.stdout.write("\x1B[H")
        sys.stdout.write(f"Przegrałeś: {reason} :(\nStatystyki:\n")
        displayNumber("Pieniądze: @ ", player.money, Fore.LIGHTYELLOW_EX)
        displayNumber("Siła: ", player.damage, Fore.MAGENTA)
        displayNumber("Liczba zabić: ", player.kills, Fore.MAGENTA)
        input("Naciśnij enter aby wyjsć")
        sys.stdout.write("\x1b[?1049l")  # switch to normal screen buffer
        sys.stdout.write("\x1b[?25l")  # hide the cursor
        exit()
