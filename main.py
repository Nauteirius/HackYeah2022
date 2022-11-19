import front, pygame, game

class game:

    currentPosition = (0,0)

    def WSADPressed(self, event):
        if event.type == pygame.K_w:
            return "UP"
        elif event.type == pygame.K_a:
            return "RIGHT"
        elif event.type == pygame.K_d:
            return "LEFT"
        elif event.type == pygame.K_s:
            return "DOWN"
        else:
            return None

    def eventLoop(self):
        while True:
            for event in pygame.event.get():
                keyName = game.WSADPressed(self, event)
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN and keyName != None:
                    game.check_before_move(self.currentPosition, keyName)


    def __init__(
                self, 
                windowSize, 
                blockSize,
                startingPosition
                ):
        front.init(windowSize, blockSize)
        self.currentPosition = startingPosition
        front.eventLoop()
        front.destroyWindow()
     
    

if __name__ == "main":
    game()