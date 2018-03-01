import unittest
from src.car import Car

print Car.__doc__

class CarTest(unittest.TestCase):
    def setUp(self):
        self.initialSpeed = 3
        self.testObject = Car(self.initialSpeed)

    def test_ctor_speed(self):
        """ctor should initialize speed field"""
        testObject = Car(9)
        assert testObject.getSpeed() == 9
    
    def test_brake_stop(self):
        """brake should stop the car"""
        self.testObject.speed = 30
        self.testObject.brake()
        assert self.testObject.speed == 0


if __name__ == "__main__":
    unittest.main() # run all tests
