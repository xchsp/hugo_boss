from pygame import *
import sys
font.init()
from math import cos,radians
try: import GetEvent
except: from . import GetEvent

def generatelvl(num):
    #Utilisation des plateform
    #
    # D M E     H   JKL
    # O I N     F
    # B P C     G   A
    if num == 1:
        lvl = [
            "DKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKI",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "F                             JKKKKKKKKKKKL                             F",
            "F                                                                       F",
            "F         JKKKKKKKKKKKL                           JKKKKKKKKKKKL         F",
            "F                                                                       F",
            "F                                                                       F",
            "F                                                                       F",
            "BKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKC",]

    elif num == 2 :
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    else :
        lvl = [
            "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPI",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "N                                                                            O",
            "IMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI",]

    return lvl;
