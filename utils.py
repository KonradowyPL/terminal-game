import os


def getChar() -> str:
    return chr(getch()[0])


if os.name == "nt":
    import msvcrt
    getch = msvcrt.getch
elif os.name == "posix":
    # A poor implementation of msvcrt.getch() for Linux

    import tty
    import sys
    import termios

    global_tmpch24b = 0

    def getch():
        global global_tmpch24b
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            if (global_tmpch24b != 0):  # Not wasting time
                return bytes([ord(lin2win())])
            tty.setraw(sys.stdin.fileno())
            ch8b = sys.stdin.read(1)
            ch24b = 0
            if (ch8b == '\x1b'):
                ch24b = ch8b + sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return bytes([ord(lin2win(ch8b, ch24b))])  # Weird encoding

    def lin2win(ch8b=None, ch24b=None):  # Weird af translating arrow key codes
        global global_tmpch24b
        if (ch24b in ['\x1b[A', '\x1b[B', '\x1b[C', '\x1b[D'] and global_tmpch24b == 0):
            global_tmpch24b = ch24b
            return 'à'

        elif (global_tmpch24b == '\x1b[A'):
            global_tmpch24b = 0
            return 'H'

        elif (global_tmpch24b == '\x1b[B'):
            global_tmpch24b = 0
            return 'P'

        elif (global_tmpch24b == '\x1b[C'):
            global_tmpch24b = 0
            return 'M'

        elif (global_tmpch24b == '\x1b[D'):
            global_tmpch24b = 0
            return 'K'

        else:
            return ch8b
else:
    raise "Unsupported operating system"
