from src.selector import menu
import sys


def startMenu():
    sys.stdout.write("\x1B[J\x1B[H")
    sys.stdout.write("Kim chcesz być:\n")

    options = [
        "Gladiator - -2 do ilości strzał, +2 do życia",
        "Łucznik - -2 do życia, +1 do obrażeń, +4 do maksymalnej ilości strzał"
    ]

    data = [
        [-2, +2, 0],
        [+4, -2, 1]

    ]

    selected = menu(options)

    selDat = data[selected]
    arrows = selDat[0] + 10
    health = selDat[1] + 10
    damage = selDat[2] + 1

    return [arrows, health, damage]
