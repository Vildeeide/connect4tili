import pygame,sys
from pygame.locals import *
import numpy as np

#hallo welt
fps = 30
windowwidth = 640
windowheight= 480
revealspeed = 8
boxsize = 40
gapsize = 10
boardwidth = 7
boardheight = 6
assert (boardwidth * boardheight)% 2 == 0, 'number of boxes needs to be even'

xmargin  = int((windowwidth - (boardwidth * (boxsize + gapsize))) / 2)
ymargin  = int((windowheight - (boardheight * (boxsize + gapsize))) / 2)

# color
gray = (100,100,100)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
boxcolor = (100,100,100)

class game:
    def __init__(self,windowwidth,windowheight,revealspeed,boxsize,gapsize,boardwidth,boardheight):
        gray = (100,100,100)
        red = (255,0,0)
        blue = (0,0,255)
        black = (0,0,0)
        white = (255,255,255)
        boxcolor = (100,100,100)
        assert (boardwidth * boardheight)% 2 == 0, 'number of boxes needs to be even'
        #
        xmargin  = int((windowwidth - (boardwidth * (boxsize + gapsize))) / 2)
        ymargin  = int((windowheight - (boardheight * (boxsize + gapsize))) / 2)
        boardArray = np.zeros((boardheight,boardwidth))

    def on__init__(self):
        #initializes pygame (it has to be started to use pygame methods/functions)
        pygame.init()
        #set the maximum framerate and the number of game loops per second
        fpsclock= pygame.time.Clock()
        #init display and size
        displaysurf = pygame.display.set_mode((windowwidth,windowheight))
        displaysurf.fill(white)
        #current mouse position
        mousex = 0
        mousey = 0
        #name of window
        pygame.display.set_caption('not memory game')
        #we dont need these
        #player1_boxes = None
        #player2_boxes = None


    def main(self):

        #game loop
        while True:
            mouseClicked = False
            displaysurf.fill(white)
            drawBoard(mainBoard,playerStones)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex,mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
            boxx, boxy = getBoxAtPixel(mousex, mousey)
            if boxx != None and boxy != None:
                pass

    def changeBoardState(self,row,collumn,player):
        boardArray[row,column] = player

    def check4win(row, column):
        directions = [(-1,-1),(-1,0),(-1,1)(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in directions:
            #reset our moves to the original coordinates
            movey = row
            movex = column
            count = 1
            while True:
                #moving through the board in the direction i
                movey += i[0]
                movex += i[1]
                #check that our algorithm does not move out of  the playing field
                if movey < 0 or movey > boardheight or movex < 0 or movex > boardwidth:
                    continue
                #check if the tile we moved to contains a stone of the player
                if boardArray[movey,movex] == boardArray[row,collumn]:
                    count +=1
                    #check if we encounterd 4 stones already
                    if count == 4:
                        break
                        won = True
                #if there is no stone or not the right stone skip this direction
                else:
                    break
            if won == True:
                break






    '''def leftTopCoordsOfBox(self,boxx,boxy):
        left = boxx *(boxsize + gapsize) + xmargin
        top = boxy *(boxsize +gapsize) + ymargin
        return (left,top)

    def getBoxAtPixel(self,x,y):
        for boxx in range (boardwidth):
            for boxy in range(boardheight):
                left,top =leftTopCoordsOfBox(boxx,boxy)
                boxRect = pygame.Rect(left,top,boxsize,boxsize)
                if boxRect.collidepoint(x,y):
                    return(boxx, boxy)
        return(None,None)

    def drawIcon(self,color,boxx,boxy):
        quarter = int(boxsize*0.25)
        half = int(boxsize*0.5)

        left, top= leftTopCoordsOfBox(boxx,boxy)
        pygame.draw.circle(displaysurf,color,(left+half,top+half),half-5)
        pygame.draw.circle(displaysurf,boxcolor,(left+half,top+half),quater-5)'''
