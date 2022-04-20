import re
from datetime import datetime
from random import randint
from faker_vehicle import VehicleProvider
import numpy as np
from faker import Faker


class CarGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')
        self.fake.add_provider(VehicleProvider)
        self.transmission = ["m", "a"]
        self.transmission_weights = [0.4, 0.6]
        self.tod = ["front", "rear", "full"]
        self.tod_weights = [0.15, 0.75, 0.1]
        self.colors = ['yellow', 'green', 'black', 'fuksia', 'white', 'gray', 'lime', 'blue',
                       'brown', 'silver', 'olive', 'purple', 'teal']
        self.type = ['wagon', 'sedan', 'convertible', 'van/minivan', 'hatchback', 'suv', 'coupe', 'pickup']

    def generate(self, amount=10):
        cars = []
        for i in range(amount):
            car = self.fake.vehicle_object()
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 0, 0, 0))
            cars.append(
                {
                    "model": "Utility.car",
                    "pk": i + 1,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "brand": car['Make'],
                        "model": car['Model'],
                        "year": car['Year'],
                        "color": np.random.choice(self.colors),
                        "type": re.split(r' |,', car['Category'])[0],
                        "mass": randint(800, 1600),
                        "transmission": np.random.choice(self.transmission, p=self.transmission_weights),
                        "tod": np.random.choice(self.tod, p=self.tod_weights),
                        "fuel_tank_capacity": randint(45, 100)
                    }
                }
            )
        return cars
