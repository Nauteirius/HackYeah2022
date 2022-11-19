class Battle():
    def __init__(self,player_army,enemy_army):
        queue = []
        for i in player_army:
            queue.append(i)
        for i in enemy_army:
            queue.append(i)
        
        queue.sort(key=lambda x: x.initiative, reverse=True)
