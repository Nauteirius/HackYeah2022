
import pygame,sys, matrix, front, battle,army



MAIN_MAP_DIMENTION = 30 #matrix of map size
SQUARE_SIZE= 32 #pixels
BATTLE_SIZE=4

object_matrix=None
player = None


background_colour = (255, 255, 255)
DisplayHandler = None
fieldSize = 30
class Window():
    def __init__(self, initialPosition, size):
        self.__position = initialPosition
        self.size=size
        #self.__textureCode = textureCode
    
    def draw(self):
        #DisplayHandler.blit( (self.__position[0]*50, self.__position[1]*50))
        DisplayHandler = pygame.display.set_mode((10*self.size, 10*self.size))

    def move(self, destination):
        self.__position = destination


class Blockade():#ustawic po prostu na wszystkie obiekty na ktore sie nie da wchodzic, czyli rzeki, drzewa, budynki(poza drzwiami do nich - tam bedzie event)
    def __init__(self):
        self.type="blockade"
    #def __init__(self,cordinates):
        #self.type="blockade"
        #object_matrix[cordinates]=self
class Zeros():
    def __init__(self):
        self.type="free"
        self.quantity=0
        self.name="zero"


class Event():
    def __init__(self,enemy_team=matrix.battleTable([Zeros(),Zeros(),Zeros(),Zeros()])):
        self.type="event"
        self.triggers=[]
        self.army = enemy_team
        self.monologue=""
        self.dialogue=""



    #def 
    
    def trigger_event(**kwargs):
        pass
        

    def trigger_monologe(self):#zwykly monolog
        print(self.monologue)
        ehh=Window((4,14),50)
        # while(True):
        #     ehh.draw()
      
        #wyswietla okno z tekstem
    def trigger_dialogue(self):#monolog + wybor gracza odpowiedzi
        print(self.dialogue)
    
    def trigger_battle(self):#enemy_coordinates
        #battle_start
        

      
        skirmish=battle.Battle(player.team,self.army)      
        #koniec bitwy, ustawimy nazwe eventu na Zero to moze zadziala
        self.type="VirtualZero"
        #object_matrix[enemy_coordinates]=Zeros() #przeciwnik znika

    def handle_event(self):
        for i in self.triggers:
            if(i=='m'):
                self.trigger_monologe()
                self.triggers.pop(0)
            if(i=='d'):
                self.trigger_dialogue(self.dialogue)
                self.triggers.pop(0)
            if(i=='b'):
                #print(self.army[0].name + "TESTTT") dotad wlacznie dziala
                self.trigger_battle()
                self.triggers.pop(0)
            if(i=='w'):
                print("Ostatecznie zwyciestwo zostalo osiagniecie, koniec gry")
                



class Player():
        def __init__(self,object_matrix):
            self.curr_pos=(0,0)

            #object_matrix[self.curr_pos]=self
            self.gold=10
            self.team=matrix.battleTable([Zeros(),Zeros(),Zeros(),Zeros()])
            self.team[0]=army.Husaria(5)
            self.team[1]=army.PiechotaWybraniecka(10)
            self.team[2]=army.Kolubryna(1)
            self.team[3]=army.PiechotaWybraniecka(10)
            self.team.quantity=4


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
    global player
    player=Player(object_matrix)



    """Deklaracja eventow"""
    event_battle1=Event(matrix.battleTable([army.Karakol(3,'k'),army.MuszkieterSzwedzki(5,'k'),Zeros(),Zeros()]))
    event_battle1.owner='k'
    event_battle1.quantity=2
    event_battle1.triggers.append('m')
    event_battle1.monologue="FOR GUSTAVUS ADOLFUS!!!!!"
    event_battle1.triggers.append('b')
    object_matrix[(4,13)]=event_battle1

    event_monologe1=Event()
    event_monologe1.monologue=("Doszly nasz sluchy wojska szwedzkie doszczednie zlupily okoliczna wioske, biada nam")
    event_monologe1.triggers.append('m')
    object_matrix[(5,2)]=event_monologe1


    event_monologe2=Event()
    event_monologe2.monologue=("Wojska nieprzyjaciela zbierają się po drugiej stronie rzeki, to ostatnia nasza szansa by ich rozbić, zanim będą zbyt si")
    event_monologe2.triggers.append('m')
    object_matrix[(12,13)]=event_monologe2


    event_battle2=Event(matrix.battleTable([army.Karakol(3,'k'),army.MuszkieterSzwedzki(5,'k'),army.Kolubryna(2,'k'),army.Karakol(5,'k')]))
    event_battle2.owner='k'
    event_battle2.quantity=4
    event_battle2.triggers.append('m')
    event_battle2.monologue="FOR GUSTAVUS ADOLFUS, AVEEEEEEE!!!!!"
    event_battle2.triggers.append('b')
    event_battle2.triggers.append('w')
    object_matrix[(4,27)]=event_battle2
    object_matrix[(2,27)]=event_battle2
    object_matrix[(3,28)]=event_battle2
    object_matrix[(3,26)]=event_battle2


    event_battle3=Event(matrix.battleTable([army.Karakol(3,'k'),army.MuszkieterSzwedzki(5,'k'),Zeros(),army.MuszkieterSzwedzki(4,'k')]))
    event_battle3.owner='k'
    event_battle3.quantity=3
    event_battle3.triggers.append('m')
    event_battle3.monologue="PRZYGOTUJ SIĘ NA ŚMIERĆ HERETYKU!!!!!"
    event_battle3.triggers.append('b')
    object_matrix[(23,19)]=event_battle3
    object_matrix[(25,19)]=event_battle3
    object_matrix[(24,20)]=event_battle3
    object_matrix[(24,18)]=event_battle3
    


    






    """ """


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
    #print(player.curr_pos ,  " OK")
    #print(correction , " OK22222")

    xpos,ypos = (player.curr_pos[0]+correction[0], player.curr_pos[1] + correction[1])
    
    if(xpos<0 or xpos>=MAIN_MAP_DIMENTION or ypos<0 or ypos>=MAIN_MAP_DIMENTION):
        return player.curr_pos
    #object_matrix = matrix.objectMatrix(MAIN_MAP_DIMENTION)

    #prawdzanie czy natrafiamy na obiekt blokujacy
    #print("xPos,yPos: " ,object_matrix[(xpos,ypos)])

    if object_matrix[(xpos,ypos)].type=="blockade":
        return player.curr_pos

    #sprawdzanie czy natrafiamy na event zdarzen
    if object_matrix[xpos,ypos].type=="event":
        #do event
        object_matrix[xpos,ypos].handle_event()
    #    handle_event(object_matrix[xpos,ypos])

    #wywoalaj te zdarzenie

    else:
        object_matrix[(xpos,ypos)]=object_matrix[player.curr_pos]
        object_matrix[player.curr_pos]=Zeros()      
        front.MovePlayer(player.curr_pos, (xpos,ypos))
        player.curr_pos=(xpos,ypos)
        return xpos,ypos



#matr









# class NPC:
#     def __init__(self):
#     self.loot=10
#     self.Army=ObjectMatrix(2)





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



     


