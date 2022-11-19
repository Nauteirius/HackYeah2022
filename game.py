import pygame,sys


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


map_matrix[][]


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
    xpos,ypos = curr_pos+correction
    if(xpos<0 or xpos>=MAIN_MAP_DIMENTION or ypos<0 or ypos>=MAIN_MAP_DIMENTION):
        pass

    #sprawdzanie czy natrafiamy na obiekt blokujacy
    if object_matrix[curr_pos + correction].type=="blockade":
        pass

    #sprawdzanie czy natrafiamy na event zdarzen
    if object_matrix[curr_pos + correction].type=="event":
        handle_event(object_matrix[curr_pos + correction])

    #wywoalaj te zdarzenie

    else:
        object_matrix[curr_pos + correction]=object_matrix[curr_pos]
        object_matrix[curr_pos]=0



def handle_event(event):
    event.
#matr

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



class Event():
    def __init__(self):
        self.triggers=[]
        self.army = [0,0,0,0]

    


    def monologue(tekst):
        #
    def(i)

class

        

        

     






