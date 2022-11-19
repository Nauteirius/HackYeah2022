
import pygame,sys, matrix, front


MAIN_MAP_DIMENTION = 30 #matrix of map size
SQUARE_SIZE= 32 #pixels
BATTLE_SIZE=4




class Game(object):
    def __init__(self):#dokumentacja, glowne klasy za co odpowiadaja
        #Config
        self.tps_max = 60.0 #liczba FPS
        self.res=1900,1080

        #1280,720
        #Initialisation
        pygame.init()
        self.screen=pygame.display.set_mode((self.res))
        self.tps_delta=0.0
        self.tps_clock = pygame.time.Clock()




def check_before_move(curr_pos,direction):
    correction=(0,0)
    if(direction=="UP"):
        correction=(0,-1)
    if(direction=="DOWN"):
        correction=(0,1)
    if(direction=="RIGHT"):
        correction=(1,0)
    if(direction=="LEFT"):
        correction=(-1,0)
    
    
    #sprawdzanie czy nie wychodzimy poza macierz
    xpos,ypos = (curr_pos[0]+correction[0], curr_pos[1] + correction[1])
    
    if(xpos<0 or xpos>=MAIN_MAP_DIMENTION or ypos<0 or ypos>=MAIN_MAP_DIMENTION):
        return curr_pos
    #object_matrix = matrix.objectMatrix(MAIN_MAP_DIMENTION)

    #sprawdzanie czy natrafiamy na obiekt blokujacy
    #if object_matrix[(xpos,ypos)].type=="blockade":
    #    pass

    #sprawdzanie czy natrafiamy na event zdarzen
    #if object_matrix[xpos,ypos].type=="event":
    #    handle_event(object_matrix[xpos,ypos])

    #wywoalaj te zdarzenie

    #else:
    #    object_matrix[xpos,ypos]=object_matrix[curr_pos]
    #    object_matrix[curr_pos]=0
    front.MovePlayer(curr_pos, (xpos,ypos))
    return xpos,ypos


def handle_event(event):
    #event.
    pass
#matr
"""
class Player():
        def __init__(self):
            self.gold=10
            self.Army=ObjectMatrix(2)
            Army[1]=
            Army[3]=

class Enemy():
    def __init__(self):
    self.loot=10
    self.Army=ObjectMatrix(2)



"""

        

        

     


