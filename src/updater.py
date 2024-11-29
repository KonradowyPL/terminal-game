import aiohttp
import asyncio
import sys
import os

URL = "https://api.github.com/repos/konradowypl/terminal-game/git/ref/heads/release"

# git rev-parse --abbrev-ref HEAD
# git rev-parse HEAD

STATUS = "checking"


async def check():
    global STATUS
    try:
        process = await asyncio.create_subprocess_exec("git", "rev-parse", "--abbrev-ref", "HEAD",
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if stdout.decode().strip() != 'release':
            # wrong branch
            STATUS = "dev"
            return

        process = await asyncio.create_subprocess_exec("git", "rev-parse", "HEAD",
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()

        commit = stdout.decode().strip()

        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                data = await response.json()
                remoteCommit = data["object"]['sha']
                if commit == remoteCommit:
                    STATUS = "newest"
                else:
                    STATUS = "old"
    except Exception:
        STATUS = "error"


def getStatus():
    return STATUS


def update():
    sys.stdout.write("\x1B[H\x1B[2J")
    sys.stdout.write("Aktualizowanie...\nPobieranie kodu...")

    os.system("git pull origin release")
    sys.stdout.write("Pobieranie bibliotek\n")
    os.system("pip install -r requirements.txt")
    sys.stdout.write("Gotowe, naciśnij enter aby kontynuować\n")
    input()
    sys.stdout.write("\x1B[H\x1B[2J")
    sys.stdout.write("\x1b[?1049l")  # switch to normal screen buffer
    sys.stdout.write("\x1b[?25h")  # show the cursor
    sys.stdout.flush()
    os.system("python main.py")
    exit()
