import aiohttp
import asyncio

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
        if stdout.decode().strip() != 'master':
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

asyncio.run(check())
print(STATUS)