class MotorCar(object):
    def __init__(self):
        """Base class constructor"""
    
class Car(MotorCar):
    def __init__(self):
        """Class constructor"""
        super(Car, self).__init__()
        
    def drive(self):
        """Drive the car"""
        
red_car = Car()
red_car.drive()

