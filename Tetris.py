import pygame
import random 

win = pygame.display.set_mode((500,700))
pygame.display.set_caption("Tetris")
pygame.init()

class player():
    def __init__(self, x, y, color):
        self.x = x 
        self.y = y
        self.color = color
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 29, 29))

class part():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 29, 29))

def generateShape():
    shapeList = ["I", "O", "T", "S", "Z", "J", "L"]
    return(shapeList[random.randint(0,6)])

def updateCompleteShape(shapeOrNextShape):
    if shapeOrNextShape == "I":
        if switch%2 == 0:
            return([part(playerShape.x, playerShape.y, (0,102,204)), part(playerShape.x, playerShape.y + 30, (0,102,204)), part(playerShape.x, playerShape.y - 30, (0,102,204)), part(playerShape.x, playerShape.y - 60, (0,102,204))])
        if switch%2 == 1:
            return([part(playerShape.x, playerShape.y, (0,102,204)), part(playerShape.x - 60, playerShape.y, (0,102,204)), part(playerShape.x - 30, playerShape.y, (0,102,204)), part(playerShape.x + 30, playerShape.y, (0,102,204))])
    if shapeOrNextShape == "O":
        return([part(playerShape.x, playerShape.y, (200,200,0)), part(playerShape.x - 30, playerShape.y, (200,200,0)), part(playerShape.x - 30, playerShape.y - 30, (200,200,0)), part(playerShape.x, playerShape.y - 30, (200,200,0))])
    if shapeOrNextShape == "T":
        if switch%4 == 0:
            return([part(playerShape.x, playerShape.y, (153,51,255)), part(playerShape.x - 30, playerShape.y, (153,51,255)), part(playerShape.x, playerShape.y - 30, (153,51,255)), part(playerShape.x + 30, playerShape.y, (153,51,255))])
        if switch%4 == 1:
            return([part(playerShape.x, playerShape.y, (153,51,255)), part(playerShape.x, playerShape.y - 30, (153,51,255)), part(playerShape.x, playerShape.y + 30, (153,51,255)), part(playerShape.x + 30, playerShape.y, (153,51,255))])
        if switch%4 == 2:
            return([part(playerShape.x, playerShape.y, (153,51,255)), part(playerShape.x - 30, playerShape.y, (153,51,255)), part(playerShape.x, playerShape.y + 30, (153,51,255)), part(playerShape.x + 30, playerShape.y, (153,51,255))])
        if switch%4 == 3:
            return([part(playerShape.x, playerShape.y, (153,51,255)), part(playerShape.x - 30, playerShape.y, (153,51,255)), part(playerShape.x, playerShape.y - 30, (153,51,255)), part(playerShape.x, playerShape.y + 30, (153,51,255))])
    if shapeOrNextShape == "S":
        if switch%4 == 0:
            return([part(playerShape.x, playerShape.y, (0,204,0)), part(playerShape.x - 30, playerShape.y, (0,204,0)), part(playerShape.x, playerShape.y - 30, (0,204,0)), part(playerShape.x + 30, playerShape.y - 30, (0,204,0))])
        if switch%4 == 1:
            return([part(playerShape.x, playerShape.y, (0,204,0)), part(playerShape.x, playerShape.y - 30, (0,204,0)), part(playerShape.x + 30, playerShape.y, (0,204,0)), part(playerShape.x + 30, playerShape.y + 30, (0,204,0))])
        if switch%4 == 2:
            return([part(playerShape.x, playerShape.y, (0,204,0)), part(playerShape.x - 30, playerShape.y, (0,204,0)), part(playerShape.x, playerShape.y - 30, (0,204,0)), part(playerShape.x + 30, playerShape.y - 30, (0,204,0))])
        if switch%4 == 3:
            return([part(playerShape.x, playerShape.y, (0,204,0)), part(playerShape.x, playerShape.y - 30, (0,204,0)), part(playerShape.x + 30, playerShape.y, (0,204,0)), part(playerShape.x + 30, playerShape.y + 30, (0,204,0))])
    if shapeOrNextShape == "Z":
        if switch%4 == 0:
            return([part(playerShape.x, playerShape.y, (255,51,51)), part(playerShape.x - 30, playerShape.y - 30, (255,51,51)), part(playerShape.x, playerShape.y - 30, (255,51,51)), part(playerShape.x + 30, playerShape.y, (255,51,51))])
        if switch%4 == 1:
            return([part(playerShape.x, playerShape.y, (255,51,51)), part(playerShape.x - 30, playerShape.y + 30, (255,51,51)), part(playerShape.x - 30, playerShape.y, (255,51,51)), part(playerShape.x, playerShape.y - 30, (255,51,51))])
        if switch%4 == 2:
            return([part(playerShape.x, playerShape.y, (255,51,51)), part(playerShape.x - 30, playerShape.y - 30, (255,51,51)), part(playerShape.x, playerShape.y - 30, (255,51,51)), part(playerShape.x + 30, playerShape.y, (255,51,51))])
        if switch%4 == 3:
            return([part(playerShape.x, playerShape.y, (255,51,51)), part(playerShape.x - 30, playerShape.y + 30, (255,51,51)), part(playerShape.x - 30, playerShape.y, (255,51,51)), part(playerShape.x, playerShape.y - 30, (255,51,51))])
    if shapeOrNextShape == "J":
        if switch%4 == 0:
            return([part(playerShape.x, playerShape.y, (160,160,160)), part(playerShape.x - 30, playerShape.y - 30, (160,160,160)), part(playerShape.x - 30, playerShape.y, (160,160,160)), part(playerShape.x + 30, playerShape.y, (160,160,160))])
        if switch%4 == 1:
            return([part(playerShape.x, playerShape.y, (160,160,160)), part(playerShape.x, playerShape.y + 30, (160,160,160)), part(playerShape.x, playerShape.y - 30, (160,160,160)), part(playerShape.x + 30, playerShape.y - 30, (160,160,160))])
        if switch%4 == 2:
            return([part(playerShape.x, playerShape.y, (160,160,160)), part(playerShape.x - 30, playerShape.y, (160,160,160)), part(playerShape.x + 30, playerShape.y, (160,160,160)), part(playerShape.x + 30, playerShape.y + 30, (160,160,160))])
        if switch%4 == 3:
            return([part(playerShape.x, playerShape.y, (160,160,160)), part(playerShape.x - 30, playerShape.y + 30, (160,160,160)), part(playerShape.x, playerShape.y + 30, (160,160,160)), part(playerShape.x, playerShape.y - 30, (160,160,160))])
    if shapeOrNextShape == "L":
        if switch%4 == 0:
            return([part(playerShape.x, playerShape.y, (255,128,0)), part(playerShape.x - 30, playerShape.y, (255,128,0)), part(playerShape.x + 30, playerShape.y, (255,128,0)), part(playerShape.x + 30, playerShape.y - 30, (255,128,0))])
        if switch%4 == 1:
            return([part(playerShape.x, playerShape.y, (255,128,0)), part(playerShape.x, playerShape.y - 30, (255,128,0)), part(playerShape.x, playerShape.y + 30, (255,128,0)), part(playerShape.x + 30, playerShape.y + 30, (255,128,0))])
        if switch%4 == 2:
            return([part(playerShape.x, playerShape.y, (255,128,0)), part(playerShape.x - 30, playerShape.y + 30, (255,128,0)), part(playerShape.x - 30, playerShape.y, (255,128,0)), part(playerShape.x + 30, playerShape.y, (255,128,0))])
        if switch%4 == 3:
            return([part(playerShape.x, playerShape.y, (255,128,0)), part(playerShape.x - 30, playerShape.y - 30, (255,128,0)), part(playerShape.x, playerShape.y - 30, (255,128,0)), part(playerShape.x, playerShape.y + 30, (255,128,0))])

def updateShapeBlockedRight(shapeBlockedRight):
    shapeBlockedRight = False
    for completeShapePart in completeShape:         
        for solidPart in solid:
            if (completeShapePart.x == solidPart.x - 30 and completeShapePart.y == solidPart.y 
            and shapeBlockedRight == False):
                shapeBlockedRight = True
    return(shapeBlockedRight)

def updateShapeBlockedLeft(shapeBlockedLeft):
    shapeBlockedLeft = False
    for completeShapePart in completeShape:
        for solidPart in solid:
            if (completeShapePart.x == solidPart.x + 30 and completeShapePart.y == solidPart.y 
            and shapeBlockedLeft == False):
                shapeBlockedLeft = True
    return(shapeBlockedLeft)

def updateShapeBlockedDown(shapeBlockedDown):
    shapeBlockedDown = False
    for completeShapePart in completeShape:
        for solidPart in solid:
           if ((completeShapePart.y == solidPart.y - 30 and completeShapePart.x == solidPart.x) 
           or (completeShapePart.y == 621)):
                shapeBlockedDown = True
    return(shapeBlockedDown)

def updateNextSwitchBlocked(nextswitchBlocked, switch):
    nextSwitchBlocked = False
    testCompleteShape = updateCompleteShape(shape)
    for testCompleteShapePart in testCompleteShape:
        for solidPart in solid:
            if ((testCompleteShapePart.x == solidPart.x and testCompleteShapePart.y == solidPart.y) 
            or testCompleteShapePart.y > 621 or testCompleteShapePart.x < 51 or testCompleteShapePart.x > 321):
                nextSwitchBlocked = True
    return(nextSwitchBlocked)

def updateLevelTimer():
    listOfTimers = {
    "level 1": 50, "level 2": 45, "level 3": 40, "level 4": 36,
    "level 5": 32, "level 6": 29, "level 7": 26, "level 8": 24,
    "level 9": 22, "level 10": 20, "level 11": 19, "level 12": 18,
    "level 13": 17, "level 14": 16, "level 15": 15, "level 16": 14,
    "level 17": 13, "level 18": 12, "level 19": 11, "level 20": 10}
    return(listOfTimers["level " + str(level)])

def clearAndUpdateRowsCleared(rowsCleared):
    for j in range(0,20):
        checkColCount = 0
        for i in range(0,10):
            checkCol = False
            for solidPart in solid:
                if (solidPart.x == 51 + 30*i and solidPart.y == 621 - 30*j):
                    checkCol = True
            if checkCol == True:
                checkColCount += 1
                checkCol = False
        if checkColCount == 10:
            rowsCleared += 1
            for solidPart in reversed(solid):
                if (solidPart.y == 621 - 30*j):
                    solid.pop(solid.index(solidPart))
            for solidPart in solid:
                if solidPart.y < 621 - 30*j:
                    solidPart.y += 30
    return(rowsCleared)

def redrawGameWindow():
    #Last Layer Drawn
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,255), (50, 50, 301, 601))
    for i in range(0,10):
        for j in range(0,20):
            pygame.draw.rect(win, (0,0,0), (51+30*i, 51+30*j, 29, 29))
    pygame.draw.rect(win, (255,255,255), (380, 80, 91, 121))
    for i in range(0,3):
        for j in range(0,4):
            pygame.draw.rect(win, (0,0,0), (381+30*i, 81+30*j, 29, 29))
    pygame.draw.rect(win,(255,255,255), (380, 260, 91, 121))
    for i in range(0,3):
        for j in range(0,4):
            pygame.draw.rect(win, (0,0,0), (381+30*i, 261+30*j, 29, 29))

    #Second Layer Drawn
    for completeShapePart in completeShape:
        completeShapePart.draw(win)
    for solidPart in solid:
        solidPart.draw(win) 
    for storedCompleteShapePart in storedCompleteShape:
        storedCompleteShapePart.draw(win)
    for completeNextShapePart in completeNextShape:
        completeNextShapePart.draw(win)
    rowsClearedText = pygame.font.SysFont('comicsans', 25).render('Rows Cleared', 1, (255,255,255))
    win.blit(rowsClearedText, (425 - (rowsClearedText.get_width()//2), 580))
    numRowsClearedText = pygame.font.SysFont('comicsans', 50).render(str(rowsCleared), 1, (255,255,255))
    win.blit(numRowsClearedText, (425 - (numRowsClearedText.get_width()//2), 610))
    storedText = pygame.font.SysFont('comicsans', 30).render('Stored', 1, (255,255,255))
    win.blit(storedText, (425 - (storedText.get_width()//2), 58))
    nextShapeText = pygame.font.SysFont('comicsans', 30).render('Next Shape', 1, (255,255,255))
    win.blit(nextShapeText, (425 - (nextShapeText.get_width()//2), 238))
    levelText = pygame.font.SysFont('comicsans', 30).render('Level ' + str(level), 1, (255,255,255))
    win.blit(levelText, (50, 30))

    #Top Layer Drawn
    if pause == True and gameOver == False:
        win.fill((100,100,100,20), None, pygame.BLEND_RGBA_MULT)
        pausedText = pygame.font.SysFont('comicsans', 300).render('II', 1, (255,255,255))
        win.blit(pausedText, (250 - (pausedText.get_width()//2), 200))
    if gameOver == True:
        win.fill((100,100,100,20), None, pygame.BLEND_RGBA_MULT)
        gameOverText = pygame.font.SysFont('comicsans', 100).render('GAME OVER', 1, (255,255,255))
        win.blit(gameOverText, (250 - (gameOverText.get_width()//2), 200))
    pygame.display.update()

run = True
nextShapeExists = False
pause = False
gameOver = False
noButtonsPressed = True
shapeBlockedRight = False
shapeBlockedLeft = False
shapeBlockedDown = False
nextSwitchBlocked = False
solid = [part(51, 651, (0,0,0))]
testCompleteShape = []
storedCompleteShape = []
switch = 0
resetPressK_RIGHTTimer = 0
resetPressK_LEFTTimer = 0
downTimer = 0
rowsCleared = 0
level = 1
levelTimer = 50
nextShape = generateShape()

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if nextShapeExists == False:
        if gameOver == False:
            nextShapeExists = True
            switch = 0
            shape = nextShape
            nextShape = generateShape()
            playerShape = player(411, 321, (0,0,0))
            completeNextShape = updateCompleteShape(nextShape)
            playerShape = player(201, 51, (0,0,0))
            completeShape = updateCompleteShape(shape)
            alreadySwitched = False

    shapeBlockedRight = updateShapeBlockedRight(shapeBlockedRight)
    shapeBlockedLeft = updateShapeBlockedLeft(shapeBlockedLeft)
    switch += 1
    nextSwitchBlocked = updateNextSwitchBlocked(nextSwitchBlocked, switch)
    switch -= 1
    
    keys = pygame.key.get_pressed()        
    
    if keys[pygame.K_p] and pause == True:
        pause = False
        pygame.time.delay (1000)
    elif keys[pygame.K_p]:
        pause = True
        pygame.time.delay(1000)

    if pause == False:
        if noButtonsPressed == True:
            if keys[pygame.K_LEFT] and shapeBlockedLeft == False and not(completeShape[1].x == 51):
                playerShape.x -= 30
                shapeBlockedDown = False
            elif keys[pygame.K_RIGHT] and shapeBlockedRight == False and not(completeShape[3].x == 321):
                playerShape.x += 30
                shapeBlockedDown = False
            if keys[pygame.K_UP] and nextSwitchBlocked == False:
                switch += 1
            if keys[pygame.K_SPACE]:
                straightDown = False
                while straightDown == False:
                    for completeShapePart in completeShape:
                        for solidPart in solid:
                            if ((completeShapePart.y + 30 == solidPart.y and completeShapePart.x == solidPart.x) 
                            or completeShapePart.y + 30 == 651):
                                straightDown = True
                    if straightDown == False:
                        playerShape.y += 30
                        completeShape = updateCompleteShape(shape)
                downTimer = 50
            if alreadySwitched == False:
                if keys[pygame.K_c]:
                    alreadySwitched = True
                    tempStoredShape = shape
                    playerShape = player(411, 141, (255,0,0))
                    switch = 0
                    completeShape = updateCompleteShape(shape)
                    storedCompleteShape = completeShape
                    try:

                        shape = storedShape
                        storedShape = tempStoredShape
                        playerShape = player(201, 51, (0,0,0))
                    except:
                        storedShape = tempStoredShape
                        nextShapeExists = False
        if keys[pygame.K_DOWN]:
            downTimer += levelTimer//5
        else:
            downTimer += 1
        
    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        resetPressK_RIGHTTimer = 0
        resetPressK_LEFTTimer = 0
    elif keys[pygame.K_RIGHT]:
        noButtonsPressed = False
        resetPressK_LEFTTimer = 0
        resetPressK_RIGHTTimer += 1
        if resetPressK_RIGHTTimer == 15:
            noButtonsPressed = True
        if resetPressK_RIGHTTimer == 25:
            noButtonsPressed = True
        if resetPressK_RIGHTTimer >= 28:
            noButtonsPressed = True
            resetPressK_RIGHTTimer = 25
    elif keys[pygame.K_LEFT]:
        noButtonsPressed = False
        resetPressK_RIGHTTimer = 0
        resetPressK_LEFTTimer += 1
        if resetPressK_LEFTTimer == 15:
            noButtonsPressed = True
        if resetPressK_LEFTTimer == 25:
            noButtonsPressed = True
        if resetPressK_LEFTTimer >= 28:
            noButtonsPressed = True
            resetPressK_LEFTTimer = 25
    elif keys[pygame.K_UP] or keys[pygame.K_c] or keys[pygame.K_SPACE]:
        noButtonsPressed = False
    else:
        noButtonsPressed = True
        resetPressK_RIGHTTimer = 0
        resetPressK_LEFTTimer = 0

    completeShape = updateCompleteShape(shape)
    shapeBlockedDown = updateShapeBlockedDown(shapeBlockedDown)
    
    level = rowsCleared//10 + 1
    if level > 20:
        level = 20
    levelTimer = updateLevelTimer()

    if downTimer >= levelTimer and shapeBlockedDown == False:
        downTimer = 0
        playerShape.y += 30
    elif downTimer >= levelTimer and shapeBlockedDown == True:
        for completeShapePart in completeShape:
            solid.append(completeShapePart)
            nextShapeExists = 0
    
    rowsCleared = clearAndUpdateRowsCleared(rowsCleared)
    
    for solidPart in solid:
        if solidPart.y <= 31:
            gameOver = True

    redrawGameWindow()
    pygame.time.delay(10)

pygame.quit()