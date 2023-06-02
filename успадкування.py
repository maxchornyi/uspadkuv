#A

class Vehicle:
    def __init__(self, make, model, weight, year):
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year
    def start_engine(self):
        print("engine works")

class Car(Vehicle):
    def __init__(self, make, model, weight, year, num_doors, num_passengers):
        super().__init__(make, model, weight, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        return "The car's engine is starting..."

    def drive(self):
        return 'car drive'

a = Vehicle('Aventador', 'Lamborgini', 2000, 2005)
print(a.start_engine())

car = Car('Aventador', 'Lamborgini', 2000, 2005, 2, 2)
print(car.drive())

#2

class Truck(Vehicle):
    def __init__(self, make, model, weight, year, cargo_capacity, towing_capacity):
        super().__init__(make, model, weight, year)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        return "The truck's engine is starting..."
    def haul(self):
        print( f"Brand {self.make}, Version {self.model}, Weight {self.weight}, Year {self.year},  Carrying capacity {self.cargo_capacity}, Maximum weight {self.towing_capacity}")
truck=Truck('Mann', 'tgx', '10т.', 2010, '20т.', '50т')
truck.haul()

#3

class Motorcycle(Vehicle):
    def __init__(self, make, model, weight, year, num_wheels, has_sidecar):
        super().__init__(make, model, weight, year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return "The motorcycle's engine is starting..."

    def ride(self):
        print(
            f"Brand {self.make}, Version {self.model}, Weight {self.weight}, Year {self.year}, Wheels {self.num_wheels}, Sidecar {self.has_sidecar}")
motorcycle=Motorcycle('Harley Davidson', 'Fat boy', '300кг.', 2023, '2', 'no')

motorcycle.ride()

print(car.start_engine())
print(truck.start_engine())
print(motorcycle.start_engine())
print(a.start_engine())
