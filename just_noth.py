class Lol:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __str__(self):
        return ("Lol ", self.num)


lol = Lol(5)
kek = Lol(1)
lol += kek
print(lol)