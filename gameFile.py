
import pygame,sys, matrix, front
#battle,army


MAIN_MAP_DIMENTION = 30 #matrix of map size
SQUARE_SIZE= 32 #pixels
BATTLE_SIZE=4

object_matrix=None
player = None

class Player():
        def __init__(self,object_matrix):
            self.curr_pos=(0,0)

            #object_matrix[self.curr_pos]=self
            self.gold=10
            self.team=matrix.battleTable([0,0,0,0])
            #self.team[1]=army.PiechotaWybraniecka()
            #self.team[3]=army.PiechotaWybraniecka()

def begin_game():
    global object_matrix
    object_matrix=matrix.objectMatrix(MAIN_MAP_DIMENTION,default_state=Zeros())
    global player
    player=Player(object_matrix)



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




def check_before_move(direction):
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
    print(player.curr_pos ,  " OK")
    print(correction , " OK22222")

    xpos,ypos = (player.curr_pos[0]+correction[0], player.curr_pos[1] + correction[1])
    
    if(xpos<0 or xpos>=MAIN_MAP_DIMENTION or ypos<0 or ypos>=MAIN_MAP_DIMENTION):
        return player.curr_pos
    #object_matrix = matrix.objectMatrix(MAIN_MAP_DIMENTION)

    #prawdzanie czy natrafiamy na obiekt blokujacy
    print("xPos,yPos: " ,object_matrix[(xpos,ypos)])

    if object_matrix[(xpos,ypos)].type=="blockade":
        pass

    #sprawdzanie czy natrafiamy na event zdarzen
    if object_matrix[xpos,ypos].type=="event":
        pass
    #    handle_event(object_matrix[xpos,ypos])

    #wywoalaj te zdarzenie

    else:
        object_matrix[(xpos,ypos)]=object_matrix[player.curr_pos]
        object_matrix[player.curr_pos]=Zeros()      
        front.MovePlayer(player.curr_pos, (xpos,ypos))
        player.curr_pos=(xpos,ypos)
        return xpos,ypos


def handle_event(event):
    #event.
    pass
#matr

class Blockade():
    def __init__(self,X,Y):
        self.type="blockade"
        object_matrix[(X,Y)]=self
class Zeros():
    def __init__(self):
        self.type="free"







# class Enemy():
#     def __init__(self):
#     self.loot=10
#     self.Army=ObjectMatrix(2)



# class Event():
#     def __init__(self,enemy_team=matrix.battleTable(4)):
#         self.triggers=[]
#         self.army = enemy_team



    
#     def trigger_event(kwargs**):
#         pass
        

#     def trigger_monologe(text):
#         pass
#         #wyswietla okno z tekstem
    
#     def trigger_battle(self.army):
#         battle=battle.start_battle(player.team,self.army)         
# class Event():
#     def __init__(self):
#         self.triggers=[]
#         self.army = [0,0,0,0]

    


#     def monologue(tekst):
#         #
#     def(i)

# class Enemy():
#     def __init__(self):
#     self.loot=10
#     self.Army=ObjectMatrix(2)



     


