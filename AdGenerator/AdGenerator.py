from datetime import datetime
from faker import Faker


class DealerAdGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')
        self.pk = 1

    def generate(self, dealer_id, ads_amount=1):
        ads = []
        for i in range(ads_amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 0))
            ad_time_start = self.fake.date_time_between(
                start_date=datetime(2022, 4, 4, 1, 0, 0),
                end_date=datetime(2022, 4, 10, 1, 0, 0)
            )
            ad_time_end = self.fake.date_time_between(
                start_date=datetime(2022, 5, 5, 1, 0, 0),
                end_date=datetime(2022, 6, 6, 1, 0, 0)
            )
            ads.append(
                {
                    "model": "Ad.dealerad",
                    "pk": self.pk,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "dealer_id": dealer_id if dealer_id else self.fake.pyint(min_value=1, max_value=100),
                        "start_date": f"{ad_time_start.year}-{ad_time_start.month}-{ad_time_start.day}T{ad_time_start.hour}:{ad_time_start.minute}:{ad_time_start.second}.123Z",
                        "end_date": f"{ad_time_end.year}-{ad_time_end.month}-{ad_time_end.day}T{ad_time_end.hour}:{ad_time_end.minute}:{ad_time_end.second}.123Z",
                        "car_id": self.fake.pyint(min_value=1, max_value=100),
                        "discount": str(self.fake.pydecimal(min_value=5, max_value=20, right_digits=2)),
                    }
                }
            )
            self.pk += 1
        return ads


class SupplierAdGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')
        self.pk = 1

    def generate(self, supplier_id=None, dealer_id=None, ads_amount=10):
        ads = []
        for i in range(ads_amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 0, 0))
            ad_time_start = self.fake.date_time_between(
                start_date=datetime(2022, 4, 4, 1, 0, 0),
                end_date=datetime(2022, 4, 10, 1, 0, 0)
            )
            ad_time_end = self.fake.date_time_between(
                start_date=datetime(2022, 5, 5, 1, 0, 0),
                end_date=datetime(2022, 6, 6, 1, 0, 0)
            )
            ads.append(
                {
                    "model": "Ad.supplierad",
                    "pk": self.pk,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "dealer_id": dealer_id if dealer_id else self.fake.pyint(min_value=1, max_value=100),
                        "supplier_id": supplier_id if supplier_id else self.fake.pyint(min_value=1, max_value=100),
                        "start_date": f"{ad_time_start.year}-{ad_time_start.month}-{ad_time_start.day}T{ad_time_start.hour}:{ad_time_start.minute}:{ad_time_start.second}.123Z",
                        "end_date": f"{ad_time_end.year}-{ad_time_end.month}-{ad_time_end.day}T{ad_time_end.hour}:{ad_time_end.minute}:{ad_time_end.second}.123Z",
                        "car_id": self.fake.pyint(min_value=1, max_value=100),
                        "discount": str(self.fake.pydecimal(min_value=5, max_value=20, right_digits=2)),
                    }
                }
            )
            self.pk += 1
        return ads
