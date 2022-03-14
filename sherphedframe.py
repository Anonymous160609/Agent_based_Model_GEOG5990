import random 

class Shepherd():
    def __init__ (self,_y,_x,colour,_acc_y,_acc_x):
        self._y = _y
        self._x = _x
        self.colour = colour
        self._acc_y = _acc_y
        self._acc_x = _acc_y
        
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "I am the 'x' property.")

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def dely(self):
        del self._y
        
    y = property(gety, sety, dely, "I am the 'y' property.")
    
    def move(self):
        if self._acc_y > 0.5:
            self._y = (self._y + 1) % 100
        else: 
            self._y = (self._y - 1) % 100
        if self._acc_x > 0.5:
            self._x = (self._x + 1) % 100
        else: 
            self._x = (self._x - 1) % 100
        self._acc_y = random.randint(0,1)
        self._acc_x = random.randint(0,1)