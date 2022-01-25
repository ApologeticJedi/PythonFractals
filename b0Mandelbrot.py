#! /usr/bin/env python
################################################################################
#                                                                              #
#  NAME:   b0Mandelbrot.py                                                     #
#  AUTHOR: Brian D. Cross (bdcross/b0c017x)                                    #
#                                                                              #
#  DESCRIPTION:                                                                #
#    Recreation of Mandelbrot's ingenius fractal                               #
#                                                                              #
################################################################################
# REVISION HISTORY.............................................................#
#       DATE    USER    DESC                                                   #
#   2019/02/26  b0c017x Creation.                                              #
################################################################################
#------------------------------------------------------------------------------#
#                               I M P O R T S                                  #
#------------------------------------------------------------------------------#
from turtle import *
from time import sleep
from math import sin, isnan

#------------------------------------------------------------------------------#
#                             F U N C T I O N S                                #
#------------------------------------------------------------------------------#
def mandelbrot_set(z , c , order):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif order > 0:
        return mandelbrot_set(z ** 2 + c, c, order - 1) 
    else:
        return z ** 2 + c

def dotmatrix_print(screenX, screenY, planeX, planeY, step, order):
    up()
    
    #convert to pixels
    pixelToX, pixelToY = (planeX[1] - planeX[0]) / screenX, (planeY[1] - planeY[0]) / screenY   
    
    # plot to X and Y
    for plotX in range(-screenX / 2, screenX / 2, int (step)):
        for plotY in range(-screenY / 2, screenY / 2, int(step)):
            x, y = plotX * pixelToX, plotY * pixelToY
            m = mandelbrot_set(0, x + 1j * y, order)
            if not isnan(m.real):
                dotcolor = [abs(sin(m.imag)) for i in range(3)]
                color(dotcolor)
                dot(2.4, dotcolor)
                goto(plotX, plotY)


#------------------------------------------------------------------------------#
#                                   M A I N                                    #
#------------------------------------------------------------------------------#
depth = 20


#Added for speed
HiSpeed = False
if HiSpeed:
    hideturtle()
    tracer(0,0)

movement = 2                                                      # discresionary step size
winX, winY = 800, 600                                             # window size (in pixels)
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)           # limits on a complex plane
setup(winX, winY)
title("Mandelbrot Fractal        (b0c017x)")
dotmatrix_print(winX, winY, complexPlaneX, complexPlaneY, movement, depth)


if HiSpeed:
    update()
    sleep(5)
