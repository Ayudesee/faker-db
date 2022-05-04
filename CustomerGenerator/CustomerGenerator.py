from datetime import datetime

from faker import Faker


class CustomerGenerator:
    def __init__(self, gender="M"):
        self.gender = gender
        self.fake = Faker('ru-RU')
        self.gender_dict = {
            "M": {
                "first_name": self.fake.first_name_male,
                "last_name": self.fake.last_name_male,
                "middle_name": self.fake.middle_name_male
            },
            "F": {
                "first_name": self.fake.first_name_female,
                "last_name": self.fake.last_name_female,
                "middle_name": self.fake.middle_name_female
            }
        }
        self.pk = 1

    def generate(self, user_id=None, amount=10, gender=None):
        if gender:
            self.gender = gender

        customers = []
        for i in range(amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 0, 0, 1))
            customers.append(
                {
                    "model": "Customer.customer",
                    "pk": user_id if user_id else self.pk,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(90),
                        "first_name": self.gender_dict[self.gender]['first_name'](),
                        "last_name": self.gender_dict[self.gender]['last_name'](),
                        "middle_name": self.gender_dict[self.gender]['middle_name'](),
                        "gender": self.gender,
                        # "email": self.fake.email(),
                        "phone_number": self.fake.phone_number(),
                        "country": self.fake.country_code(),
                        "balance": str(self.fake.pydecimal(min_value=0, max_value=200_000, right_digits=2))
                    }
                }
            )
            self.pk += 1
        return customers
