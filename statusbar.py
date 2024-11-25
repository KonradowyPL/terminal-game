import sys
from colorama import Fore


def displayStatus(icon: str, maxNum: int, crurent: int, colorActive: str, colorInactive: str, charActive: str, charInactive: str):
    sys.stdout.write(colorActive + icon + charActive * crurent + colorInactive +
                     charInactive * (maxNum - crurent) + Fore.RESET + f" {crurent}/{maxNum}" + " "*20 + "\n")


def displayNumber(icon, number, color):
    sys.stdout.write(color + icon + f"{number}" + Fore.RESET + " "*20 + "\n")
