
#dwuwymiarowa macierz zawierająca obiekty gry

class objectMatrix:
    __firstDimention = []
    __size = 0
    def __init__(self, size):
        self.__size = size
        for x in range(size):
            self.__firstDimention.append([0] * size)
    
    def getSize(self):
        return self.__size

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
            self.__firstDimention[position[0]][position[1]] = newvalue
    


