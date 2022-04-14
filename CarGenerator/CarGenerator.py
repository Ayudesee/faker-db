from datetime import datetime
from random import randint
from faker_vehicle import VehicleProvider
import numpy as np
from faker import Faker


class CarGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')
        self.fake.add_provider(VehicleProvider)
        self.transmission = ["Manual", "Automatic"]
        self.transmission_weights = [0.4, 0.6]
        self.tod = ["Front", "Rear", "Full"]
        self.tod_weights = [0.15, 0.75, 0.1]

    def generate(self, amount=10):
        cars = {}
        for i in range(amount):
            car = self.fake.vehicle_object()
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 0, 0, 0))
            cars[i + 1] = {
                "model": "Utility.car",
                "pk": i + 1,
                "fields": {
                    "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                    "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                    "is_active": self.fake.boolean(95),
                    "brand": car['Make'],
                    "model": car['Model'],
                    "year": car['Year'],
                    "description": {
                        "type": car['Category'],
                        "mass": randint(800, 1600),
                        "transmission": np.random.choice(self.transmission, p=self.transmission_weights),
                        "Type of drive": np.random.choice(self.tod, p=self.tod_weights),
                        "Fuel tank capacity": randint(45, 100)
                    }
                }
            }
        return cars
