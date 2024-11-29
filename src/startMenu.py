from src.selector import menu, COLOR_UNSELECTED
from src.updater import getStatus, check, update

import asyncio
import sys

options = [
    "Gladiator - -2 do ilości strzał, +2 do życia",
    "Łucznik - -2 do życia, +1 do obrażeń, +4 do maksymalnej ilości strzał\n"
]


async def startMenu():
    sys.stdout.write("\x1B[J\x1B[H")
    sys.stdout.write("Kim chcesz być:\n")

    data = [
        [-2, +2, 0],
        [+4, -2, 1]

    ]
    asyncio.create_task(log())
    asyncio.create_task(check())
    selected = await menu(options)

    if selected == len(options) - 1:
        update()
        exit()

    selDat = data[selected]
    arrows = selDat[0] + 10
    health = selDat[1] + 10
    damage = selDat[2] + 1

    return [arrows, health, damage]


async def log():
    # spinner = "⠈⠐⠠⠄⠂⠁"
    spinner = "⠃⠉⠘⠰⠤⠆"
    while getStatus() == "checking":
        for char in spinner:
            sys.stdout.write(f"\r{char} Sprawdzanie aktualizacji")
            sys.stdout.flush()
            await asyncio.sleep(0.1)

    if getStatus() == "error":
        msg = "Nie można spawdzić aktualizacji :("
    elif getStatus() == "dev":
        msg = "Jej, dev!"
    elif getStatus() == "newest":
        msg = "Używasz najnowszej wersji!"
    elif getStatus() == "old":
        msg = "Wybież aby zaktualizować!"
    else:
        msg = "Nastąpił nieoczekiwany błąd w sprawdzaniu aktualizacji :("

    sys.stdout.write(f"\r  {COLOR_UNSELECTED}{msg}" + " " * 20)
    sys.stdout.flush()
    options.append(msg)
