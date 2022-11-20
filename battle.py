import random#, import gameFile

class Battle():
    def __init__(self,player_army,enemy_army):
        self.queue = []
        self.battle_ended=0
        for i in player_army:
            self.queue.append(i)
        for i in enemy_army:
            self.queue.append(i)
        
        self.queue.sort(key=lambda x: x.initiative, reverse=True)
        self.start_battle(self,player_army,enemy_army,battle_ended=0)#zacznij bitwe

    def start_battle(self,player_army,enemy_army):
        while(self.battle_ended==0):
            current = self.queue[0]

            

            #jesli kolej gracza:
            if(current.affilation=="player"):
                can_be_damaged= current.who_can_shot()
                

            #jesli kolej komputera
            else:
                current.do_damage(random.choice(current.who_can_shot(player_army)),player_army)

            self.queue.append(current)
            self.queue.pop(0)

    #matrix.frontdead()
    def end_battle(self,matrix):
        self.battle_ended=1
        if matrix.owner=='p':
            pass
            #victory
            #display scren for 5 minutes
        else:
            self.game_over()
            

    def game_over():
        pass
    #display window which says przegrana
    #terminate game after few seconds
    def do_damage(self,target,matrix):#matrix:player_army or enemy_army

        #wykonaj animacje uderzenia
        #zmien na czerwono na sekunde

        modifier = 1 # tymczasowo do zmiany pozniej
        damage=(self.attack/target.defence)*self.quantity * modifier
        deads=(damage+target.max_hp-target.current_hp)//target.max_hp
        target.current_hp=damage%target.max_hp
        target.quantity-=deads
        if target.quantity<=0:
            target.quantity=0
            #dead unit!!
            matrix[matrix.getcoordinates(target)]=0
            matrix.quantity-=1
            if(matrix.quantity<=0):
                end_battle(matrix)





        








        
