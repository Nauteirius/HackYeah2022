
import pygame,sys, matrix, front, battle,army



MAIN_MAP_DIMENTION = 30 #matrix of map size
SQUARE_SIZE= 32 #pixels
BATTLE_SIZE=4

object_matrix=None
player = None



class Blockade():#ustawic po prostu na wszystkie obiekty na ktore sie nie da wchodzic, czyli rzeki, drzewa, budynki(poza drzwiami do nich - tam bedzie event)
    def __init__(self):
        self.type="blockade"
    #def __init__(self,cordinates):
        #self.type="blockade"
        #object_matrix[cordinates]=self
class Zeros():
    def __init__(self):
        self.type="free"




class Player():
        def __init__(self,object_matrix):
            self.curr_pos=(0,0)

            #object_matrix[self.curr_pos]=self
            self.gold=10
            self.team=matrix.battleTable([0,0,0,0])
            #self.team[1]=army.PiechotaWybraniecka()
            #self.team[3]=army.PiechotaWybraniecka()


map_event=[Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),
 Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),
 Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),
 Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),
 Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Blockade(),Blockade(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),
 Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Blockade(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),
 Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Blockade(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros(),Zeros()]



def begin_game():
    mapSize=30
    global object_matrix
    object_matrix=matrix.objectMatrix(MAIN_MAP_DIMENTION,default_state=Zeros())

    for x in range(mapSize):
        for y in range(mapSize):
            object_matrix[(x,y)] = map_event[y*mapSize + x]
            # if(y==2):
            #     print(object_matrix[(x,y)])



    #######################################################################################
    #object_matrix[]




    ######################################################################################
    global player
    player=Player(object_matrix)
    #b1=Blockade((2,2))



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
        return player.curr_pos

    #sprawdzanie czy natrafiamy na event zdarzen
    if object_matrix[xpos,ypos].type=="event":
        #do event
        return
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









# class NPC:
#     def __init__(self):
#     self.loot=10
#     self.Army=ObjectMatrix(2)



class Event():
    def __init__(self,cordinates,enemy_team=matrix.battleTable([0,0,0,0])):
        self.type="event"
        self.triggers=[]
        self.army = enemy_team



    #def 
    
    def trigger_event(**kwargs):
        pass
        

    def trigger_monologe(text):
        pass
        #wyswietla okno z tekstem
    def trigger_dialogue(text):
        pass
    
    def trigger_battle(self,enemy_army,enemy_coordinates):
        #battle_start
        

      
        battle=battle.start_battle(player.team,enemy_army)      
        #koniec bitwy, ustawimy nazwe eventu na Zero to moze zadziala
        self.type="VirtualZero"
        object_matrix[enemy_coordinates]=Zeros() #przeciwnik znika
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



     


