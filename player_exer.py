class Player:
    '''
    Something about player.
    '''

    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

    def __str__(self):
        return f'''
        Player Instance
        gold_coins = {self.gold_coins}
        health_points = {self.health_points}
        lives = {self.lives}
        '''

    def level_up(self):
        self.lives += 1
        return self.lives

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()
    
    def do_battle(self, damage):
        if self.health_points < 1:
            self.lives - 1 and self.health_points == 10
        elif self.lives < 1:
            self.restart()


    def restart(self):
        self.gold_coins = 0 
        self.health_points = 10 
        self.lives = 5
        
        


player1 = Player(50, 30, 10)
player1.collect_treasure()






    