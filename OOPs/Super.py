class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type) #super method
        super().start()
        super().stop()

Car1 = ToyotaCar("fortuner","electric")
print(Car1.type)