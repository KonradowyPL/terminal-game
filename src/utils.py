import os
import sys
import asyncio

if os.name == "nt":
    import msvcrt

    async def getch():
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, msvcrt.getch)

elif os.name == "posix":
    import tty
    import termios

    global_tmpch24b = 0

    async def getch():
        global global_tmpch24b
        loop = asyncio.get_running_loop()

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            if global_tmpch24b != 0:  # Return previously stored multi-byte key
                return bytes([ord(lin2win())])

            tty.setraw(fd)
            ch8b = await loop.run_in_executor(None, sys.stdin.read, 1)
            ch24b = 0
            if ch8b == '\x1b':  # Escape sequence (e.g., arrow keys)
                ch24b = ch8b + await loop.run_in_executor(None, sys.stdin.read, 2)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return bytes([ord(lin2win(ch8b, ch24b))])

    def lin2win(ch8b=None, ch24b=None):
        global global_tmpch24b
        if (ch24b in ['\x1b[A', '\x1b[B', '\x1b[C', '\x1b[D'] and global_tmpch24b == 0):
            global_tmpch24b = ch24b
            return 'à'

        elif global_tmpch24b == '\x1b[A':
            global_tmpch24b = 0
            return 'H'

        elif global_tmpch24b == '\x1b[B':
            global_tmpch24b = 0
            return 'P'

        elif global_tmpch24b == '\x1b[C':
            global_tmpch24b = 0
            return 'M'

        elif global_tmpch24b == '\x1b[D':
            global_tmpch24b = 0
            return 'K'

        else:
            return ch8b
else:
    raise Exception("Unsupported operating system")


async def getChar() -> str:
    return chr((await getch())[0])
