
#dwuwymiarowa macierz zawierająca obiekty gry

class objectMatrix:
    __firstDimention = []
    __size = 0
    #__object_count = 0
    def __init__(self, size,default_state):
        self.__firstDimention = []
        self.__size = size
        self.__object_count = 0
        for x in range(size):
            self.__firstDimention.append([default_state] * size)
    
    def getSize(self):
        return self.__size

    #def getObjectCount(self):
    #    return self.__object_count

    def belongsTo(self, object):
        for x in range(self.__size):
            for y in range(self.__size):
                if self[(x,y)] == object:
                    return True
        return False

    def __getitem__(self,
                    position    #pozycja
                    ):  #złe indeksowanie: null
        if (position[0] >= 0 and position[0] < self.__size) and (position[1] >= 0 and position[1] < self.__size):
            return self.__firstDimention[ position[0]][position[1]]
        else:
            return None

    def __setitem__(self,
                    position,
                    newvalue
                    ):
        if (position[0] >= 0 and position[0] < self.__size) and (position[1] >= 0 and position[1] < self.__size):
      #      val =  self.__firstDimention[position[0]][position[1]]
     #       if val != 0 and newvalue == 0:
       #         self.__object_count -= 0
        #    elif val == 0 and newvalue != 0:
        #        self.__object_count += 1
            self.__firstDimention[position[0]][position[1]] = newvalue
    


class battleTable(list):
    __obj_count = 0
    def __init__(self, *args):
        self.__obj_count = 0
        list.__init__(self, *args)

    def __setitem__(self, index, newvalue):
        if self[index] == 0 and newvalue != 0:
            self.__obj_count -= 1
        elif self[index] != 0 and newvalue == 0:
            self.__obj_count += 1
        list.__setitem__(self,index,newvalue)