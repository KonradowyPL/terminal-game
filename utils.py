import colorama


def getChar() -> str:
    import msvcrt
    return chr(msvcrt.getch()[0])
