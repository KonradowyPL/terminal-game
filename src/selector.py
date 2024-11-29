import sys
from colorama import Fore, Style
from src.utils import getChar



COLOR_SELECTED = Fore.BLUE + Style.BRIGHT
COLOR_UNSELECTED = Fore.CYAN + Style.NORMAL
COLOR_RESET = Style.RESET_ALL

TEXT_SELECTED = "> " + COLOR_SELECTED
TEXT_UNSELECTED = "  " + COLOR_UNSELECTED


async def menu(options, selected = 0):
    sys.stdout.write("\x1B[s")  # save cursor position
    sys.stdout.write("\x1B[?25l")  # hide the cursor
    
    while True:
        sys.stdout.write("\x1B[u")  # restore saved cursor position

        for index, option in enumerate(options):
            sys.stdout.write(TEXT_SELECTED if index ==
                             selected else TEXT_UNSELECTED)
            sys.stdout.write(option)
            sys.stdout.write(COLOR_RESET + "\n")

        sys.stdout.flush()
        char = await getChar()

        # Exit on Ctrl+C
        if char == "\x03":
            raise KeyboardInterrupt

        # Handle arrow key presses
        if char == 'à':  # Special key prefix
            char = await getChar()
            if char == "H":  # Up arrow
                selected -= 1
            elif char == "P":  # Down arrow
                selected += 1

        # Keep selection within bounds
        selected = min(selected, len(options) - 1)
        selected = max(selected, 0)

        # Return selection on Enter
        if char == "\r":
            sys.stdout.write("\x1B[u")  # restore saved cursor position
            return selected