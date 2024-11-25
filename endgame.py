from statusbar import displayNumber
from colorama import Fore
import sys

def end(player):
        sys.stdout.write("Statystyki:\n")
        displayNumber("Pieniądze: @ ", player.money, Fore.LIGHTYELLOW_EX)
        displayNumber("Siła: ", player.damage, Fore.MAGENTA)
        displayNumber("Liczba zabić: ", player.kills, Fore.MAGENTA)
        input("Naciśnij enter aby wyjsć")
        sys.stdout.write("\x1B[2J")
        exit()
