import matrix, random
mapSize = 15

Map = [int(random.random() + 0.5) + 1 for i in range(mapSize ** 2) ] #int(random.Random().random()*1) for i in range(mapSize**2) ]
mapMatrix = matrix.objectMatrix(mapSize)
for x in range(mapSize):
    for y in range(mapSize):
        mapMatrix[(x,y)] = Map[y*mapSize + x]


textureAmount = 3
textureFiles = [ 'texture' + str(i) +'.png' for i in range(textureAmount) ]
