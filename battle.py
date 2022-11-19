class Battle():
    def __init__(self,player_army,enemy_army):
        self.queue = []
        for i in player_army:
            self.queue.append(i)
        for i in enemy_army:
            self.queue.append(i)
        
        self.queue.sort(key=lambda x: x.initiative, reverse=True)

    def start_battle():
        while(True):
            currect = self.queue[0]
            
            #jesli kolej gracza:
            #currect.#jesli dziedziczy po piechocie
            
            if(wybor==enemymatrix[1] or wybor==enemymatrix[3]):
                do_damage
            

            else:
                "zly wybor"

    #matrix.frontdead()
    def end_battle(matrix):
        if matrix.dokogonaleze==Game.player:
            #victory
        else:
            #game over
            

    def do_damage(self,target,matrix):#matrix:player_army or enemy_army
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





        








        
