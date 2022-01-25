#! /usr/bin/env python
################################################################################
#                                                                              #
#  NAME:   b0PeanoSpace.py                                                     #
#  AUTHOR: Brian D. Cross (bdcross/b0c017x)                                    #
#                                                                              #
#  DESCRIPTION:                                                                #
#    Recreation of the David Hilbert solution for the Peano Space Fractal      #
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
def hilbertPeano(length, order, parity):
    if order == 0:
        return

    #rotate and draw the first subcurve with opposite parity to big curve
    left(parity * 90)
    hilbertPeano(length, order - 1, -parity)

    #interface to and draw second subcurve with same parity as big curve
    forward(length)
    right(parity * 90)
    hilbertPeano(length, order - 1, parity)

    # third subcurve
    forward(length)
    hilbertPeano(length, order - 1, parity)

    #fourth subcurve
    right(parity * 90)
    forward(length)
    hilbertPeano(length, order - 1, -parity)
    
    #a final turn is neede to make the turtle end up facing outward from the large square
    left(parity * 90)


#------------------------------------------------------------------------------#
#                                   M A I N                                    #
#------------------------------------------------------------------------------#
depth = 5

wheel=12
title("Peano Space - David Hilbert variation      (b0c017x)")
speed(0)
hilbertPeano(6, depth, 1)
hideturtle()
sleep(2)
