# Add your Python code here. E.g.
from microbit import *
import random

class Character:
    def __init__(self, xLoc, yLoc):
        self.x = xLoc
        self.y = yLoc

class Bullet:
    x = 0
    y = 0

player = Character(2, 4)

enemy = Character(0, 0)

def drawCharacter(c):
    display.set_pixel(c.x, c.y, 9)

def clearBoard():
    display.clear()
    
def enemyJump(e):
    e.x = e.x + random.randint(-1,1)
    e.y = e.y + random.randint(-1,1)
    if e.x < 0:
        e.x = 4
    elif e.x > 4:
        e.x = 0
    
    if e.y < 0:
        e.y = 4
    elif e.y > 4:
        e.y = 0

bullet = Bullet()
bullet.x = 5
ticker = 0
while True:
    if ticker > 5:
        ticker = 0
    if enemy.x == player.x and enemy.y == player.y:
        clearBoard()
        display.scroll("You lose....")
        display.show(Image.SAD)
        while True:
            sleep(60000)
    if enemy.x == bullet.x and enemy.y == bullet.y:
        clearBoard()
        display.scroll("You win!")
        display.show(Image.HAPPY)
        while True:
            sleep(60000)
        
    aPress = button_a.was_pressed()
    bPress = button_b.was_pressed()
        
    if aPress and bPress:
        if bullet.x == 5:
            bullet.x = player.x
            bullet.y = player.y
    elif aPress:
        if player.x != 0:
            player.x = player.x - 1
    elif bPress:
        if player.x != 4:
            player.x += 1
    clearBoard()
    if bullet.x < 5:
        bullet.y = bullet.y - 1
        if bullet.y <0:
            bullet.x = 5
        else:
            display.set_pixel(bullet.x,bullet.y, 4)
    if ticker > 4:
        enemyJump(enemy)

    drawCharacter(player)
    drawCharacter(enemy)
    ticker += 1
    sleep(500)
