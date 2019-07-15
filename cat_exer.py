class Cat:
    '''
    Soomehting about the cat
    '''
    # Constructor
    def __init__(self, name , preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f"The cat {self.name} likes to eat {self.preferred_food} at the time of {self.meal_time} "

    def eats_at(self):
        if self.meal_time >= 12:
            return self.meal_time - 12
        else:
            return self.meal_time

    def meow(self):
        return f'Hi I am {self.name} and I like to eat {self.preferred_food} at {self.meal_time}'




   


    

moo = Cat('Moo', 'tuna + temptations', 12)
pete = Cat('Pete', 'whiskas', 18)

print(pete.eats_at())
print(moo.meow())
print(pete.meow())



