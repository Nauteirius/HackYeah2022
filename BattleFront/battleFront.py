import pygame
from button import Button

background =  (255,255,255)


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


    def chooseEnemyUnit(self):