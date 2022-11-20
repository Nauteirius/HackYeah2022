import pygame
from button import Button

background =  (255,255,255)
squareSize = 90


class BattleFront():
    def __init__(self, displayHandle):
        self.displayHandle = displayHandle

    def draw(self, player_army_strings, enemy_army_strings, queue_strings):
        self.displayHandle.fill(background)

        imagePlayerUnit = []
        for i in range(0,3):
            imagePlayerUnit[i] = pygame.image.load(player_army_strings[i])

        imageEnemyUnit = []
        for i in range(0,3):
            imageEnemyUnit[i] = pygame.image.load(enemy_army_strings[i])

        imageQueue = []
        for i in range(0,7):
            imageQueue[i] = pygame.image.load(queue_strings[i])

        #wypisuje kolejke
        queueLevel = 4
        for i in range(0,7):
            self.displayHandle.blit(imageQueue[i], (squareSize*(i+1), squareSize*queueLevel))
        #wypisuje swoja armie
        beginHeightPlayerArmy = 1
        beginWeightPlayerArmy = 1
        self.displayHandle.blit(imagePlayerUnit[0],
                                (beginWeightPlayerArmy*squareSize, beginHeightPlayerArmy*squareSize))
        self.displayHandle.blit(imagePlayerUnit[1],
                                (beginWeightPlayerArmy * squareSize, (beginHeightPlayerArmy+1) * squareSize))
        self.displayHandle.blit(imagePlayerUnit[2],
                                ((beginWeightPlayerArmy+1) * squareSize, beginHeightPlayerArmy * squareSize))
        self.displayHandle.blit(imagePlayerUnit[3],
                                ((beginWeightPlayerArmy+1) * squareSize, (beginHeightPlayerArmy + 1) * squareSize))
        #wypisuje armie wrogie
        beginHeightPlayerArmy = 1
        beginWeightPlayerArmy = 7
        self.displayHandle.blit(imageEnemyUnit[0],
                                (beginWeightPlayerArmy * squareSize, beginHeightPlayerArmy * squareSize))
        self.displayHandle.blit(imageEnemyUnit[1],
                                (beginWeightPlayerArmy * squareSize, (beginHeightPlayerArmy + 1) * squareSize))
        self.displayHandle.blit(imageEnemyUnit[2],
                                ((beginWeightPlayerArmy + 1) * squareSize, beginHeightPlayerArmy * squareSize))
        self.displayHandle.blit(imageEnemyUnit[3],
                                ((beginWeightPlayerArmy + 1) * squareSize, (beginHeightPlayerArmy + 1) * squareSize))

    def chooseEnemyUnit(self):