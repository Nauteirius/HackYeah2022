from time import sleep
import random#, import gameFile

class Battle():
    def __init__(self,player_army,enemy_army):
        self.queue = []
        self.battle_ended=0
        for i in player_army:
            if(i.name=="zero"):continue
            self.queue.append(i)
        for i in enemy_army:
            if(i.name=="zero"):continue
            self.queue.append(i)
            #print(i.name)
        
        self.queue.sort(key=lambda x: x.initiative, reverse=True)
        self.start_battle(player_army,enemy_army)#zacznij bitwe

    def start_battle(self,player_army,enemy_army):
        #print("BATTLE STARTED")
        while(self.battle_ended==0):
            current = self.queue[0]

            sleep(1)
            #print("ITS STILL GOING")
            for test in self.queue:
                pass
                #print (test.name)

            #jesli kolej gracza:
            if(current.affilation=='p'):
                can_be_damaged= current.who_can_shot(enemy_army)#to jest indeks dopiero
                #mozesz wybrac jedno z okienek na ktore wskazuje zmienna can_be_damaged,
                #if() wybrales opcje ta - wtedy zycie traci ten
                #czyli petla

            #jesli kolej komputera
            else:
                self.do_damage(current,player_army[random.choice(current.who_can_shot(player_army))],player_army)
                sleep(1)

            self.queue.append(current)
            self.queue.pop(0)

    #matrix.frontdead()
    def end_battle(self,matrix):
        self.battle_ended=1
        if matrix.owner=='k':#pokonany komputer
            print("victory")
            sleep(2)
            print("victory")
            #display scren for 5 seconds
        else:
            self.game_over()
            

    def game_over(self):
        while(True):
            print("GAME OVER")
    #display window which says przegrana
    #terminate game after few seconds
    def do_damage(self,we,target,matrix):#matrix:player_army or enemy_army

        #wykonaj animacje uderzenia
        #zmien na czerwono na sekunde

        modifier = 1 # tymczasowo do zmiany pozniej
        damage=(we.attack/target.defence)*we.quantity * modifier
        deads=(damage+target.max_hp-target.current_hp)//target.max_hp
        target.current_hp=damage%target.max_hp
        target.quantity-=deads
        print(we.name , "zadal: ",damage, "obrazen " , target.name , ", zabil " , deads ,", zostalo przy zyciu: " , target.quantity)
        if target.quantity<=0:
            target.quantity=0
            #dead unit!!
            #usunac z listy inicjatywy
            self.queue.remove(matrix[matrix.get_coordinates(target)])
            print(matrix[matrix.get_coordinates(target)].name + "DIED!")
            matrix[matrix.get_coordinates(target)]=Zeros2()
            matrix.quantity-=1
            if(matrix.quantity<=0):
                self.end_battle(matrix)
            
            
            


class Zeros2():
    def __init__(self):
        self.type="free"
        self.quantity=0
        self.name="zero"


        








        
