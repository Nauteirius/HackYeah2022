class Army():#dac zmienna czy nalezy do 
        def __init__(self):
            self.attack
            self.defence
            self.initiative
            self.hp
            self.quantity
            self.pos

        def assault():
            #wybierz okno przeciwnika ktorego ma zaatakowac
            pass

            
        
        #def checker(object):
            #if(object pos)

        

class Infranty(Army):
    
    def who_can_shot(self,matrix):
        
        
        #sprawdzic na ktorej pozycji jest self, ostrzal z tylnego szeregu tylko jesli w przednim nikogo nie ma
        #####################################
        #
        #
        #
        #
        #####################################

        if(matrix[1].name=="zero" and matrix[3].name=="zero"):
            if(matrix[0].name=="zero"):
                return [2]
            if(matrix[2].name=="zero"):
                return [0]
            else: return [2,4]
        else:
            if(matrix[1].name=="zero"):
                return [3]
            if(matrix[3].name=="zero"):
                return [1]
            else: return [1,3]



class Cavarly(Army):
    def who_can_shot(self,matrix):
        result = []
        for i,j in enumerate(matrix):
            if(j.name!="zero"):result.append(i)
        return result

class Artilery(Army):
    def who_can_shot(self,matrix):
        result = []
        for i,j in enumerate(matrix):
            if(j.name!="zero"):result.append(i)
        return result




class MuszkieterSzwedzki(Infranty):
   
    def __init__(self,quan=1,af='p'):
        self.attack=50
        self.defence=30
        self.initiative=10
        self.current_hp=5
        self.current_hp=5
        self.quantity=quan
        self.affilation=af
        self.texture=""
        self.name = "Muszkieter Szwedzki"


class PiechotaWybraniecka(Infranty):


    def __init__(self,quan=1,af='p'):
        self.attack=30
        self.defence=50
        self.initiative=10
        self.max_hp=5
        self.current_hp=5
        self.quantity=quan
        self.affilation=af
        self.texture=""
        self.name = "Piechota Wybraniecka"


class Husaria(Cavarly):
    def __init__(self,quan=1,af='p'):
        self.attack=180
        self.defence=80
        self.initiative=25
        self.max_hp=10
        self.current_hp=10
        self.quantity=quan
        self.affilation=af
        self.texture=""
        self.name = "Husaria"

class Karakol(Cavarly):
    def __init__(self,quan=1,af='p'):
        self.attack=80
        self.defence=80
        self.initiative=20
        self.max_hp=10
        self.current_hp=10
        self.quantity=quan
        self.affilation=af
        self.texture=""
        self.name = "Karakol"

class Kolubryna(Artilery):
    def __init__(self,quan=1,af='p'):
        self.attack=180
        self.defence=3
        self.initiative=3
        self.max_hp=3
        self.current_hp=3
        self.quantity=quan
        self.affilation=af
        self.texture=""
        self.name = "Kolubryna"



