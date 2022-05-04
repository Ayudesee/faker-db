from datetime import datetime

from faker import Faker


class DealerGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')

    def generate(self, user_id=None, amount=10):
        dealers = []
        for i in range(amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 0))
            dealers.append(
                {
                    "model": "Dealer.dealer",
                    "pk": user_id if user_id else i + 1,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "name": self.fake.company(),
                        "country": self.fake.country_code(),
                        "location": f"{self.fake.city()} {self.fake.street_address()}",
                        "balance": str(self.fake.pydecimal(min_value=200_000, max_value=5_200_000, right_digits=2))
                    }
                }
            )
        return dealers
