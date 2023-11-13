import maya.cmds as cmds
import random

def randomplacement(randomX,randomY,randomZ,numberOfObjects):

    ojSleceted = cmds.ls(slection = True,) # get all sleceted objects

    if ojSleceted == 0:
        cmds.error("Make a slection before running Randomplacement")

    if ojSleceted >= 0:
        i = 0

        while i < numberOfObjects:
            cmds.duplicate( ojSleceted[i], rr = True)

            xMove = random.uniform(randomX[0],randomX[1])
            yMove = random.uniform(randomY[0],randomY[1])
            zMove = random.uniform(randomZ[0],randomZ[1])

            cmds.move(xMove, yMove, zMove, ojSleceted,worldspace =True, r = True)

            i+= 1

randomplacement([],[],[],[])