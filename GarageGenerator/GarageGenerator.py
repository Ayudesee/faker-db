from datetime import datetime

from faker import Faker


class DealerGarageGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')

    def generate(self, car_amount=25, dealers_amount=10):
        garages = []
        dealers = []
        for dealer in range(dealers_amount):
            cars = []
            d_int = self.fake.pyint(min_value=1, max_value=100)
            while d_int in dealers:
                d_int = self.fake.pyint(min_value=1, max_value=100)
            dealers.append(d_int)
            for i in range(car_amount):
                car = self.fake.pyint(min_value=1, max_value=100)
                while car in cars:
                    car = self.fake.pyint(min_value=1, max_value=100)
                cars.append(car)
                time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 0))
                garages.append(
                    {
                        "model": "Utility.dealergarage",
                        "pk": i + 1,
                        "fields": {
                            "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                            "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                            "is_active": self.fake.boolean(95),
                            "dealer_id": d_int,
                            "car_id": cars[-1],
                            "amount": self.fake.pyint(min_value=1, max_value=25),
                        }
                    }
                )
        return garages


class SupplierGarageGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')

    def generate(self, car_amount=25, suppliers_amount=10):
        garages = []
        suppliers = []
        for dealer in range(suppliers_amount):
            cars = []
            s_int = self.fake.pyint(min_value=1, max_value=100)
            while s_int in suppliers:
                s_int = self.fake.pyint(min_value=1, max_value=100)
            suppliers.append(s_int)
            for i in range(car_amount):
                car = self.fake.pyint(min_value=1, max_value=100)
                while car in cars:
                    car = self.fake.pyint(min_value=1, max_value=100)
                cars.append(car)
                time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 0))
                garages.append(
                    {
                        "model": "Utility.suppliergarage",
                        "pk": i + 1,
                        "fields": {
                            "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                            "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                            "is_active": self.fake.boolean(95),
                            "supplier_id": s_int,
                            "car_id": self.fake.pyint(min_value=1, max_value=100),
                            "amount": self.fake.pyint(min_value=100, max_value=525),
                        }
                    }
                )
        return garages
