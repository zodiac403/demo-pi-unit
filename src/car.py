class Car:
    """Unit under test."""

    def __init__(self, speed):
        self.speed = speed
    
    def getSpeed(self):
        return self.speed

    def brake(self):
        self.speed = 0
