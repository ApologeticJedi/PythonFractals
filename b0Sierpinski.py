#! /usr/bin/env python
################################################################################
#                                                                              #
#  NAME:   b0Sierpinski.py                                                     #
#  AUTHOR: Brian D. Cross (bdcross/b0c017x)                                    #
#                                                                              #
#  DESCRIPTION:                                                                #
#    Recreation of the Waclaw Sierpinski Gasket using triangles.               #
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
#                             F U N C T I O N S                                #
#------------------------------------------------------------------------------#
def getMidPoint(pointA, pointB):
    return ( ( pointA[0] + pointB[0]) / 2, ( pointA[1] + pointB[1]) / 2)

def sierpinskiTriangle(points, order):
    up()
    goto(points[0][0],points[0][1])
    down()
    goto(points[1][0],points[1][1])
    goto(points[2][0],points[2][1])
    goto(points[0][0],points[0][1])

    if order > 0:
        sierpinskiTriangle([points[0], getMidPoint(points[0], points[1]), getMidPoint(points[0], points[2])], order - 1)
        sierpinskiTriangle([points[1], getMidPoint(points[0], points[1]), getMidPoint(points[1], points[2])], order - 1)
        sierpinskiTriangle([points[2], getMidPoint(points[2], points[1]), getMidPoint(points[0], points[2])], order - 1)

#------------------------------------------------------------------------------#
#                                   M A I N                                    #
#------------------------------------------------------------------------------#
depth = 6

wheel=12
title("Sierpinski Gasket        (b0c017x)")
speed(0)
points = [[-175,-125],[0,175],[175,-125]]
sierpinskiTriangle(points, depth)
hideturtle()
sleep(2)
