# Marie Leung (mcleung)

## 15-112 Term Project: "I Can't Sleep" ##

from tkinter import *
import random
import time # time.time() difference

## Init

def init(data):
    data.mode = "titleScreen"
    
    # title margins
    data.leftMargin = (2/3) * data.width
    data.margin0 = (3/8) * data.height
    data.margin1 = data.height // 2
    data.margin2 = (5/8) * data.height
    data.margin3 = (3/4) * data.height
    data.margin4 = (7/8) * data.height
    
    # nav margins
    data.backArrowX = 90 # right side
    data.backArrowY = data.height - 120 # top
    data.startButtonX = data.width//2 - 80
    data.startButtonY = data.height//2 + 270
    data.startButtonW = 160
    data.startButtonH = 50
    
    # images
    data.titleBG = PhotoImage(file="cityruinstitle.gif")
    data.levelBG = PhotoImage(file="cityruins.gif")
    
    # colors
    data.M4col = "purple1"
    data.SRcol = "deeppink"
    data.pyroCol = "darkorange"
    
    # playable size: 2560 x 1440
    # viewable size: 3840 x 1800
    data.playRectX = -640
    data.playRectY = -360
    data.playRectW = 2 * data.width
    data.playRectH = 2 * data.height
    data.xScroll = data.width // 20
    data.yScroll = data.height // 20
    data.timerCalls = 0
    
    # game info
    data.player = "M4"
    data.bullets = []
    
    # enemy info
    data.enemyR = 40


## Classes

# Players

class Player(object):
    def __init__(self, health, attack, defense, damage=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.damage = damage
    
    def takeDmg(self):
        if self.damage - self.defense > 0:
            return self.health - (self.damage - self.defense)
        else:
            return self.health
    
    def hp(self):
        return self.health
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class M4(Player): # standard hitscan gun
    def __init__(self, health, attack, defense, damage=0):
        super().__init__(self, health, attack, defense, damage)
    
    def attack(self):
        return self.attack

class SR(Player): # high damage gun but have to scope
    def __init__(self, health, attack, defense, scope=False, damage=0):
        super().__init__(self, health, attack, defense, damage)
        self.scope = scope
    
    def scoped(self, event):
        if self.scope == False and event.num == "Button-3":
            self.scope = True
        elif self.scope == True and event.num == "Button-3":
            self.scope = False
    
    def attack(self):
        if self.scope:
            return self.attack

class Pyro(Player): # burns enemies
    def __init__(self, health, attack, defense, damage=0):
        super().__init__(self, health, attack, defense, damage)
    
    def attack(self):
        if data.timerCalls % 5 == 0 and event.num == "Button-1":
            return self.attack

# Enemies
    
class MiniEnemy(object):
    def __init__(self, x, y, health, attack, damage=0):
        self.health = health
        self.attack = attack
        self.damage = damage
    
    def attack(self):
        return self.attack
    
    def takeDmg(self):
        return self.health - self.damage
    
    def hp(self):
        return self.health
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def draw(self, canvas):
        canvas.create_oval(self.x - data.enemyR, self.y - data.enemyR,
                           self.x + data.enemyR, self.y + data.enemyR,
                           fill="white")

# class NumEnemy(MiniEnemy):
#     def __init__(self, health, attack, damage=0):
#         super().__init__(self, health, attack, damage)
#     
#     def draw(self, canvas):
#         pass
# 
# # little number icons that deal damage of their number
# 
# class GraphicEnemy(MiniEnemy):
#     def __init__(self, health, attack, damage=0):
#         super().__init__(self, health, attack, damage)
# 
# class CircleEnemy(GraphicEnemy):
#     def __init__(self, health, attack, damage=0):
#         super().__init__(self, health, attack, damage)
#     
#     def draw(self, canvas):
#         pass
# 
# class SquareEnemy(GraphicEnemy):
#     def __init__(self, health, attack, damage=0):
#         super().__init__(self, health, attack, damage)
#     
#     def draw(self, canvas):
#         pass
# 
# class TriangleEnemy(GraphicEnemy):
#     def __init__(self, health, attack, damage=0):
#         super().__init__(self, health, attack, damage)
    
    def draw(self, canvas):
        pass

# boss probably doesn't need class since there's only one

class Bullet(object):
    def __init__(self, x, y, r=10):
        self.x = x
        self.y = y
    
    def draw(self, canvas):
        if (data.player == "M4"):
            bulletCol = data.M4col
        elif (data.player == "SR"):
            bulletCol = data.SRcol
        elif (data.player == "Pyro"):
            bulletCol = data.pyroCol
        canvas.create_oval(self.x - self.r, self.y - self.r, 
                           self.x + self.r, self.y + self.r,
                           fill=bulletCol)
    
    def move(self):
        self.y -= 1

## Helper Functions

def drawAmmo():
    pass

def dropAmmo(): # drops ammo pack from sky, will be on timer of 10s
    pass

# add map collision with "houses"

## Modes

def mousePressed(event, data):
    if (data.mode == "titleScreen"):
        titleScreenMousePressed(event, data)
    elif (data.mode == "instructions"):
        instructionsMousePressed(event, data)
    elif (data.mode == "controlScreen"):
        controlScreenMousePressed(event, data)
    elif (data.mode == "charSelect"):
        charSelectMousePressed(event, data)
    elif (data.mode == "gameMode"):
        gameModeMousePressed(event, data)
    elif (data.mode == "deathScreen"):
        deathScreenMousePressed(event, data)
        
def keyPressed(event, data):
    if (data.mode == "titleScreen"):
        titleScreenKeyPressed(event, data)
    elif (data.mode == "instructions"):
        instructionsKeyPressed(event, data)
    elif (data.mode == "controlScreen"):
        controlScreenKeyPressed(event, data)
    elif (data.mode == "charSelect"):
        charSelectKeyPressed(event, data)
    elif (data.mode == "gameMode"):
        gameModeKeyPressed(event, data)
    elif (data.mode == "deathScreen"):
        deathScreenKeyPressed(event, data)
        
def timerFired(data):
    if (data.mode == "titleScreen"):
        titleScreenTimerFired(data)
    elif (data.mode == "instructions"):
        instructionsTimerFired(data)
    elif (data.mode == "controlScreen"):
        controlScreenTimerFired(data)
    elif (data.mode == "charSelect"):
        charSelectTimerFired(data)
    elif (data.mode == "gameMode"):
        gameModeTimerFired(data)
    elif (data.mode == "deathScreen"):
        deathScreenTimerFired(data)
        
def redrawAll(canvas, data):
    if (data.mode == "titleScreen"):
        titleScreenRedrawAll(canvas, data)
    elif (data.mode == "instructions"):
        instructionsRedrawAll(canvas, data)
    elif (data.mode == "controlScreen"):
        controlScreenRedrawAll(canvas, data)
    elif (data.mode == "charSelect"):
        charSelectRedrawAll(canvas, data)
    elif (data.mode == "gameMode"):
        gameModeRedrawAll(canvas, data)
    elif (data.mode == "deathScreen"):
        deathScreenRedrawAll(canvas, data)
        
## MODE: titleScreen

def titleScreenMousePressed(event, data):
    if (event.x > data.leftMargin and event.y > data.margin0 and 
        event.y < data.margin1):
        data.mode = "charSelect" # "New Game"
    elif (event.x > data.leftMargin and event.y > data.margin1 and 
          event.y < data.margin2):
        pass # "Load Game"
    elif (event.x > data.leftMargin and event.y > data.margin2 and 
          event.y < data.margin3):
        data.mode = "instructions" # "How to Play"
    elif (event.x > data.leftMargin and event.y > data.margin3 and 
          event.y < data.margin4):
        pass # "Quit"

def titleScreenKeyPressed(event, data):
    pass # done

def titleScreenTimerFired(data):
    pass # done

def titleScreenRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor=NW, image=data.titleBG)
    
    canvas.create_text(data.width/5, data.height/5, text="I Can't Sleep",
                       font="Arial 26 bold") # placeholder; all text will be 
                                # part of the background graphics I'm creating
    canvas.create_text(data.width/5, data.height/5 + 40,
                       text="A Journey of 112", font="Arial 20 bold")
    canvas.create_text(data.leftMargin, data.margin0, text="New Game", 
                       anchor=NW, font="Arial 26", fill="white")
    canvas.create_text(data.leftMargin, data.margin1, text="Load Game", 
                       anchor=NW, font="Arial 26", fill="white")
                       # saves enemy count, time survived, kills, player
    canvas.create_text(data.leftMargin, data.margin2, text="Instructions", 
                       anchor=NW, font="Arial 26", fill="white")
    canvas.create_text(data.leftMargin, data.margin3, text="Quit", 
                       anchor=NW, font="Arial 26", fill="white")

## MODE: instructions

def instructionsMousePressed(event, data):
    if (event.x < data.backArrowX and event.y > data.backArrowY):
        data.mode = "titleScreen"

def instructionsKeyPressed(event, data):
    pass # done

def instructionsTimerFired(data):
    pass # done

def instructionsRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/8,
                       text="Instructions", font="Arial 26 bold")
    canvas.create_text(data.backArrowX, data.backArrowY, text="<", anchor=NE,
                       font="Arial 80 bold")

## MODE: controlScreen

def controlScreenMousePressed(event, data):
    pass # done

def controlScreenKeyPressed(event, data):
    if (event.char == "c"):
        data.mode = "gameMode"

def controlScreenTimerFired(data):
    pass # done

def controlScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/8,
                       text="Controls", font="Arial 26 bold")
    canvas.create_text(data.width/2, (7/8) * data.height,
                       text="Press [C] to return to game", font="Arial 20 bold")

## MODE: charSelect

def charSelectMousePressed(event, data):
    if (event.x > data.startButtonX and 
        event.x < data.startButtonX + data.startButtonW and
        event.y > data.startButtonY and
        event.y < data.startButtonY + data.startButtonH):
        data.mode = "gameMode"

def charSelectKeyPressed(event, data):
    charList = ["M4", "SR", "Pyro"]
    for i in range(len(charList)):
        if (charList[i] == data.player):
            curPlayerIndex = i
        if (event.keysym == "LEFT"):
            if (i == 0):
                curPlayerIndex = 2
            else:
                curPlayerIndex -= 1
        elif (event.keysym == "RIGHT"):
            if (i == 2):
                curPlayerIndex = 0
            else:
                curPlayerIndex += 1
    data.player = charList[curPlayerIndex]
    print("Current selection: ", data.player)

def charSelectTimerFired(data):
    pass # done

def charSelectRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/8,
                       text="Character Selection", font="Arial 26 bold")
    canvas.create_rectangle(data.startButtonX, data.startButtonY,
                            data.startButtonX + data.startButtonW,
                            data.startButtonY + data.startButtonH, fill="")
    canvas.create_text(data.width//2,
                       data.startButtonY + (.5 * data.startButtonH),
                       text="START", font="Arial 26 bold")

## MODE: gameMode

def gameModeMousePressed(event, data):
    # if (event.num == "Button-1"):
    #     newBul = Bullet(data.width//2, data.height)
    #     data.bullets.append(newBul)
    pass
        

def gameModeKeyPressed(event, data):
    if (event.char == 'w' and data.playRectY < data.height//2): # look up
        data.playRectY += data.yScroll
    if (event.char == 'a' and data.playRectX < data.width//2): # look left
        data.playRectX += data.xScroll
    if (event.char == 's' and 
        data.playRectY + data.playRectH > data.height): # look down
        data.playRectY -= data.yScroll
    if (event.char == 'd' and 
        data.playRectX + data.playRectW > data.width//2): # look right
        data.playRectX -= data.xScroll
    if (event.char == 'q'): # lean left with gun
        pass # think of it tilting left and right like a speedometer
    if (event.char == 'e'): # lean right with gun
        pass

    # testing
    elif (event.char == 'c'):
        data.mode = "controlScreen"
    elif (event.char == 'n'): # for testing purposes
        data.mode = "deathScreen"
    elif (event.char == 'm'): # for testing purposes
        data.mode = "titleScreen"
    
    if (event.keysym == "SPACE"):
        newBul = Bullet(data.width//2, data.height)
        data.bullets.append(newBul)

def gameModeTimerFired(data):
    data.timerCalls += 1 # 0.1s
    for bullet in data.bullets:
        bullet.move()

def gameModeRedrawAll(canvas, data):
    canvas.create_image(data.playRectX - data.width//2, 
                        data.playRectY - data.height//2, 
                        anchor=NW, image=data.levelBG) # will improve graphics
    canvas.create_rectangle(data.playRectX, data.playRectY, 
                            data.playRectX + data.playRectW, 
                            data.playRectY + data.playRectH,
                            fill="", outline="white") # test for stopping scroll
    
    canvas.create_text(data.width//2, data.height//3,
                       text="Testing controls: [N] = end game, [M] = main menu",
                       font="Arial 26 bold") # for testing purposes
    canvas.create_text(data.playRectX + data.width,
                       data.playRectY + data.height, text="board center",
                       font="Arial 16") # for testing purposes
    
    # bullets
    for bullet in data.bullets:
        bullet.draw()

## MODE: deathScreen

def deathScreenMousePressed(event, data):
    if (event.x > data.startButtonX and 
        event.x < data.startButtonX + data.startButtonW and
        event.y > data.startButtonY and
        event.y < data.startButtonY + data.startButtonH):
        data.mode = "titleScreen"

def deathScreenKeyPressed(event, data):
    pass # done

def deathScreenTimerFired(data):
    pass # done

def deathScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/4,
                       text="Game Over!", font="Arial 26 bold")
    canvas.create_rectangle(data.startButtonX, data.startButtonY,
                            data.startButtonX + data.startButtonW,
                            data.startButtonY + data.startButtonH, fill="")
    canvas.create_text(data.width//2,
                       data.startButtonY + (.5 * data.startButtonH),
                       text="MAIN MENU", font="Arial 16 bold")

## RUN!!

def run(width=1280, height=720):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def rightMousePressedWrapper(event, canvas, data):
        rightMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Toplevel()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Button-3>", lambda event:
                            rightMousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Running I CAN'T SLEEP...")

run()