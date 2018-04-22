# Marie Leung (mcleung)

## 15-112 Term Project: "I Can't Sleep" ##

from tkinter import *
import random

## Init

def init(data):
    data.mode = "titleScreen"
    data.leftMargin = (2/3) * data.width
    data.margin0 = (3/8) * data.height
    data.margin1 = data.height // 2
    data.margin2 = (5/8) * data.height
    data.margin3 = (3/4) * data.height
    data.margin4 = (7/8) * data.height
    data.backArrowX = 90 # right side
    data.backArrowY = data.height - 120 # top
    data.startButtonX = data.width//2 - 80
    data.startButtonY = data.height//2 + 270
    data.startButtonW = 160
    data.startButtonH = 50
    
    # playable size: 2560 x 1440
    # viewable size: 3840 x 1800
    data.playRectX = -640
    data.playRectY = -360
    data.playRectW = 2 * data.width
    data.playRectH = 2 * data.height
    data.xScroll = data.width // 20
    data.yScroll = data.height // 20
    
    data.titleBG = PhotoImage(file="cityruinstitle.gif")
    data.levelBG = PhotoImage(file="cityruins.gif")

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

class Sniper(Player): # high damage gun but have to scope
    def __init__(self, health, attack, defense, scope=False, damage=0):
        super().__init__(self, health, attack, defense, damage)
        self.scope = scope
    
    def scoped(self, event):
        if self.scope == False and event.x: # RIGHT CLICK?
            self.scope = True
        elif self.scope == True and event.x:
            self.scope = False
    
    def attack(self):
        if self.scope:
            return self.attack
        else:
            return 0

class Pyro(Player): # burns enemies
    def __init__(self, health, attack, defense, damage=0):
        super().__init__(self, health, attack, defense, damage)
    # how to do damage over time?

# Enemies
    
class MiniEnemy(object):
    def __init__(self, health, attack, damage=0):
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

class NumEnemy(MiniEnemy):
    def __init__(self, health, attack, damage=0):
        super().__init__(self, health, attack, damage)
    
    def draw(self, canvas):
        pass

# little number icons that deal damage of their number

class GraphicEnemy(MiniEnemy):
    def __init__(self, health, attack, damage=0):
        super().__init__(self, health, attack, damage)

class CircleEnemy(GraphicEnemy):
    def __init__(self, health, attack, damage=0):
        super().__init__(self, health, attack, damage)
    
    def draw(self, canvas):
        pass

class SquareEnemy(GraphicEnemy):
    def __init__(self, health, attack, damage=0):
        super().__init__(self, health, attack, damage)
    
    def draw(self, canvas):
        pass

class TriangleEnemy(GraphicEnemy):
    def __init__(self, health, attack, damage=0):
        super().__init__(self, health, attack, damage)
    
    def draw(self, canvas):
        pass

# boss probably doesn't need class since there's only one

## Helper Functions

def drawBullet(): # draw circle
    pass

def fireBullet(): # call drawBullet() at correct trajectories
    pass

def drawAmmo():
    pass

def dropAmmo(): # drops ammo pack from sky, will be on timer of 10s
    pass

def drawBoss():
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
    pass

def titleScreenTimerFired(data):
    pass

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
    canvas.create_text(data.leftMargin, data.margin2, text="Instructions", 
                       anchor=NW, font="Arial 26", fill="white")
    canvas.create_text(data.leftMargin, data.margin3, text="Quit", 
                       anchor=NW, font="Arial 26", fill="white")

## MODE: instructions

def instructionsMousePressed(event, data):
    if (event.x < data.backArrowX and event.y > data.backArrowY):
        data.mode = "titleScreen"

def instructionsKeyPressed(event, data):
    pass

def instructionsTimerFired(data):
    pass

def instructionsRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/8,
                       text="Instructions", font="Arial 26 bold")
    canvas.create_text(data.backArrowX, data.backArrowY, text="<", anchor=NE,
                       font="Arial 80 bold")

## MODE: controlScreen

def controlScreenMousePressed(event, data):
    pass

def controlScreenKeyPressed(event, data):
    if (event.char == "c"):
        data.mode = "gameMode"

def controlScreenTimerFired(data):
    pass

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
    pass

def charSelectTimerFired(data):
    pass

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
    pass # will fire gun at whatever trajectory was determined by 'Q' and 'E'

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

    elif (event.char == 'c'):
        data.mode = "controlScreen"
    elif (event.char == 'n'): # for testing purposes
        data.mode = "deathScreen"
    elif (event.char == 'm'): # for testing purposes
        data.mode = "titleScreen"

def gameModeTimerFired(data):
    pass

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

## MODE: deathScreen

def deathScreenMousePressed(event, data):
    if (event.x > data.startButtonX and 
        event.x < data.startButtonX + data.startButtonW and
        event.y > data.startButtonY and
        event.y < data.startButtonY + data.startButtonH):
        data.mode = "titleScreen"

def deathScreenKeyPressed(event, data):
    pass

def deathScreenTimerFired(data):
    pass

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
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Running I CAN'T SLEEP...")

run()