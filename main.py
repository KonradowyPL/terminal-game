import sys
from colorama import just_fix_windows_console, Fore
import schedculer
from spawner import spawner
from world import World
from player import Player
from shop import Shop, shopSelector
from projectile import Arrow
from utils import getChar
from statusbar import displayStatus, displayNumber
from endgame import end
from startMenu import startMenu

shopMsg = "Nasiśnij enter aby wejść do sklepu"


def main():
    just_fix_windows_console()
    arrows, health, damage = startMenu()
    # print(Fore.RED + "Heloł łord" + Fore.RESET)
    world = World()
    player = Player(y=3*4, x=1, maxHelath=health, damage=damage, maxArrows=arrows)
    world.addEntity(player)
    shop = Shop()
    world.addEntity(shop)

    spawner(1, world, player)

    sys.stdout.flush()


# TODE wft is this
    while True:
        schedculer.tick()
        char = getChar()

        # Exit on Ctrl+C
        if char == "\x03":
            raise KeyboardInterrupt

        # Handle arrow key presses
        if char == 'à':  # Special key prefix
            char = getChar()
            player.move(char)
        elif char == "\r" and (player.x == shop.x and player.y == shop.y):
            sys.stdout.write("\x1B[H\x1B[2J")
            shopSelector(player)
            sys.stdout.write("\x1B[2J")
            world.render()
        elif char == " " and player.arrows > 0:
            player.arrows -= 1
            arrow = Arrow(player.x, player.y+1, 5, 0, player.damage)
            world.addEntity(arrow)

        # update entities
        for entity in world.entities[::-1]:
            # check if has ben deleted this frame
            if not entity in world.entities:
                continue
            entity.frame()
            entity.render()

        # check player death
        if player.health <= 0:
            end(player, "Zginąłeś")


        # redner gui
        sys.stdout.write("\x1B[H")
        displayStatus("♥ ", player.maxHealth, player.health,
                      Fore.LIGHTRED_EX, Fore.LIGHTBLACK_EX, "=", "=")

        displayStatus("↑ ", player.maxArrows, player.arrows,
                      Fore.LIGHTBLUE_EX, Fore.LIGHTBLACK_EX, "-", "`")

        displayNumber("@ ", player.money, Fore.LIGHTYELLOW_EX)

        if player.x == shop.x and player.y == shop.y:
            sys.stdout.write(shopMsg)
        else:
            sys.stdout.write(" " * len(shopMsg))

        sys.stdout.flush()


if __name__ == "__main__":
    try:
        sys.stdout.write("\x1b[?25l")  # hide the cursor
        sys.stdout.write("\x1b[?1049h")  # switch to alternate screen buffer
        main()
    except KeyboardInterrupt:
        pass
    sys.stdout.write("\x1b[?1049l")  # switch to normal screen buffer
    sys.stdout.write("\x1b[?25l")  # hide the cursor
    
