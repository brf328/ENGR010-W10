import random
import matplotlib as plt
from math import cos

def plot(function, x):
    plt.plot(x, function(x))
    plt.show()

class Chooser:
    def __init__(self, values=None):
        if values is None:
            self.values = [1, 2, 3, 4, 5, 6]
        else:
            self.values = values
        self.current_value = random.choice(self.values)

    def get_value(self):
        return self.current_value

    def select(self):
        self.current_value = random.choice(self.values)
        return self.current_value
    
class Die(Chooser):
    def __init__(self):
        super().__init__(values=[1, 2, 3, 4, 5, 6])

    def roll(self):
        return self.select()
    

if __name__ == "__main__":
    print("test code")
    x = [x for x in range(10)]
    plt.plot(cos(x), x)
    die1 = Die()
    print(die1.roll)
    choose = Chooser()
    print(choose.select)