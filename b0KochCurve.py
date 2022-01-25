#! /usr/bin/env python
################################################################################
#                                                                              #
#  NAME:   b0KochCurve.py                                                      #
#  AUTHOR: Brian D. Cross (bdcross/b0c017x)                                    #
#                                                                              #
#  DESCRIPTION:                                                                #
#    Recreation of the Koch Curve fractal solution by Helge Von Koch           #
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
def koch(length, order):
    if order == 0:
        forward(length)
    else:
        for turn in [60, -120, 60, 0]:
            koch(length/3, order-1)
            left(turn)

def snowflake(length, order):
    for turn in [120, 120, 0]:
        koch(length, order)
        right(turn)
    

#------------------------------------------------------------------------------#
#                                   M A I N                                    #
#------------------------------------------------------------------------------#
depth = 4
wheel=12
title("Koch Curve     (b0c017x)")
speed(0)
snowflake(300,depth)
hideturtle()
sleep(2)
