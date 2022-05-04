from datetime import datetime
from random import randint

from faker import Faker


class SupplierGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')

    def generate(self, user_id=None, amount=10):
        suppliers = []
        for i in range(amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 1))
            suppliers.append(
                {
                    "model": "Supplier.supplier",
                    "pk": user_id if user_id else i + 1,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "name": f"{self.fake.company()} {self.fake.company_suffix()}",
                        "country": self.fake.country_code(),
                        "location": f"{self.fake.city()} {self.fake.street_address()}",
                        "foundation_year": randint(1890, 1960)
                    }
                }
            )
        return suppliers
