#! /usr/bin/env python
################################################################################
#                                                                              #
#  NAME:   b0CantorSet.py                                                      #
#  AUTHOR: Brian D. Cross (bdcross/b0c017x)                                    #
#                                                                              #
#  DESCRIPTION:                                                                #
#    This is a flipped version of the traditional cantor tenary set. Credit    #
#    to the original mathematical introduction by Georg Cantor. Instead of     #
#    erasing the middle third, I am simply drawing around it.                  #
#                                                                              #
################################################################################
# REVISION HISTORY.............................................................#
#       DATE    USER    DESC                                                   #
#   2019/02/25  b0c017x Creation.                                              #
################################################################################
#------------------------------------------------------------------------------#
#                               I M P O R T S                                  #
#------------------------------------------------------------------------------#
from turtle import *
from time import sleep


#------------------------------------------------------------------------------#
#                               G L O B A L S                                  #
#------------------------------------------------------------------------------#
HEIGHT = 20

#------------------------------------------------------------------------------#
#                             F U N C T I O N S                                #
#------------------------------------------------------------------------------#
def drawLine(posX, posY, length):
    up()
    setpos(posX, posY)
    down()
    forward(length)

def cantorLine(posX, posY, length, order):
    if order == 0:
        return
    drawLine(posX, posY, length)
    #draw first third of original line
    cantorLine(posX,                posY + HEIGHT, length / 3, order - 1)
    #draw final third of original line
    cantorLine(posX + length * 2/3, posY + HEIGHT, length / 3, order - 1)

#------------------------------------------------------------------------------#
#                                   M A I N                                    #
#------------------------------------------------------------------------------#
beginX = -300
beginY = -300
beginLen = 600
order = 6
pensize(1)
title("Cantor Ternary Set     (b0c017x)")

#draw 1/4th which is always in cantor set, but never an endpoint
#drawLine(beginX, beginY, beginLen / 4)

# Move up to start the actual cantor set
cantorLine(beginX, beginY+HEIGHT, beginLen, order)
hideturtle()
sleep(2)
