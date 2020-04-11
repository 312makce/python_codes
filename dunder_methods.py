class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'Garage with {len(self)} cars'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('focus')

#for car in ford:
#    print(car)
print(ford)
