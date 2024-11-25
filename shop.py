from copyreg import constructor
from gui import RenderableComponent
import selector
import sys
from colorama import Style, Fore
from statusbar import displayNumber, displayStatus



class Shop(RenderableComponent):
    def __init__(self):
        image = [
            
"/SKLEP\\",
" | D | ",
" |   | ",
" |   | ",
        ]
        x = 1
        y = 4*3
        super().__init__(image, x, y)


# 0:name
# 1: target dict ele
# 2: target max ele
# 3:amount
# 4: cost

offers = [
    ["Strzały x3", "arrows", "maxArrows", 3, 3],
    ["Rozmiar kołczanu", "maxArrows", "infinity", 10, 10],
    ["Zbroja", "maxHealth", "infinity", 4, 10],
    ["Mikstura leczenia", "health", "infinity", 5, 4],
    ["Lepsze strzały", "damage", "infinity", 1, 5],
]


def shopSelector(player):

    selected = 0
    while True:
        sys.stdout.write("\x1B[J\x1b[H")
        sys.stdout.write("Witaj w sklepie!\n")
        sys.stdout.write("Uzyj strzałek aby wybrać, uzyj enter aby kupić\n")
        displayStatus("↑ ", player.maxArrows, player.arrows,
                      Fore.LIGHTBLUE_EX, Fore.LIGHTBLACK_EX, "-", "`")

        displayNumber("@ ", player.money, Fore.LIGHTYELLOW_EX)
        sys.stdout.write("Statystyki:\n")
        displayNumber("Siła: ", player.damage, Fore.MAGENTA)
        displayNumber("Liczba zabić: ", player.kills, Fore.MAGENTA)

        sys.stdout.write("\n")

        options = ["Wyjdź ze sklepu"]

        for offer in offers:
            text = offer[0]
            if player.__dict__[offer[2]] < player.__dict__[offer[1]] + offer[3] or player.money < offer[4]:
                text+= f" ({offer[4]} @)" +  " (Nie możesz teko kupić)"
            else:
                text += f"{Fore.LIGHTYELLOW_EX} ({offer[4]} @)"

            options.append(text)

        selected = selector.menu(options, selected=selected)

        if selected == 0:
            return
        offer = offers[selected-1]

        if player.__dict__[offer[2]] >= player.__dict__[offer[1]] + offer[3] and player.money >= offer[4]:
            player.__dict__[offer[1]] += offer[3]
            player.money -= offer[4]
