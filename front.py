#front end package
import map, pygame

background_colour = (255, 255, 255)
DisplayHandler = None
fieldSize = 30
player = None
INITIAL_PLAYER_POSITION = (0,0)
textures = None
DEFAULT_IMAGE_SIZE = (fieldSize, fieldSize)



class frontPlayer:
    def __init__(self, initialPosition, textureCode):
        self.__position = initialPosition
        self.__textureCode = textureCode
    
    def draw(self):
        DisplayHandler.blit(textures[self.__textureCode], (self.__position[0]*fieldSize, self.__position[1]*fieldSize))

    def move(self, destination):
        self.__position = destination

class frontNPC:
    def __init__(self, initialPosition, textureCode):
        self.__position = initialPosition
        self.__textureCode = textureCode
    
    def draw(self):
        DisplayHandler.blit(textures[self.__textureCode], (self.__position[0]*fieldSize, self.__position[1]*fieldSize))


def init(
        windowSize,
        blockSize
        ):
    global DisplayHandler, textures, player, npc_monologue1,npc_battle1,npc_monologue2,npc_battle2,npc_battle3
    DisplayHandler = pygame.display.set_mode((windowSize*blockSize, windowSize*blockSize))
    DisplayHandler.fill(background_colour)
    player = frontPlayer(INITIAL_PLAYER_POSITION, 0)
    npc_monologue1=frontNPC((5,2),8)
    npc_monologue2=frontNPC((12,13),8)
    npc_battle1=frontNPC((4,14),9)
    npc_battle2=frontNPC((3,27),9)
    npc_battle3=frontNPC((24,19),9)
    
    textures = [pygame.transform.scale(pygame.image.load(map.textureFiles[i]), DEFAULT_IMAGE_SIZE)  for i in range(map.textureAmount)]


def draw():
    for x in range(map.mapMatrix.getSize()):
        for y in range(map.mapMatrix.getSize()):
            #print(map.mapMatrix[(x,y)])
            #textures[map.mapMatrix[(x,y)]] #tu sie wywala
            DisplayHandler.blit(textures[map.mapMatrix[(x,y)]], (x * fieldSize, y * fieldSize))
    player.draw()
    npc_monologue1.draw()
    npc_battle1.draw()
    npc_monologue2.draw()
    npc_battle2.draw()
    npc_battle3.draw()

    pygame.display.flip()
    pygame.display.update()

    
def MovePlayer(currentPosition, destination):
    #print(destination)
    player.move(destination)