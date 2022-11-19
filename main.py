import front, pygame, gameFile

class game:

    currentPosition = (0,0)

    def WSADPressed(self, event):
        if event.type != pygame.KEYDOWN:
            return None
        if event.key == pygame.K_w:
            return "UP"
        elif event.key == pygame.K_a:
            return "LEFT"
        elif event.key == pygame.K_d:
            return "RIGHT"
        elif event.key == pygame.K_s:
            return "DOWN"
        else:
            return None

    def eventLoop(self):
        isRunning = True
        while isRunning:
            for event in pygame.event.get():
                keyName = game.WSADPressed(self, event)
                if event.type == pygame.QUIT:
                    isRunning = False
                    break
                elif event.type == pygame.KEYDOWN and keyName != None:
                    print('x', keyName)
                    self.currentPosition = gameFile.check_before_move(self.currentPosition, keyName)
                    front.draw()
                    print(self.currentPosition)


    def __init__(
                self, 
                windowSize, 
                blockSize,
                startingPosition
                ):
        front.init(windowSize, blockSize)
        front.draw()
        self.currentPosition = startingPosition
        self.eventLoop()
        print('x')
        front.destroyWindow()
     
    

if __name__ == "__main__":
    game(30, 30, (0,0))