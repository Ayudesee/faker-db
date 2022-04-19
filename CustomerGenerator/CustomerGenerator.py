from datetime import datetime

from faker import Faker


class CustomerGenerator:
    def __init__(self, sex="M"):
        self.sex = sex
        self.fake = Faker('ru-RU')
        self.sex_dict = {
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

    def generate(self, amount=10, sex=None):
        if sex:
            self.sex = sex

        customers = []
        for i in range(amount):
            time = self.fake.date_time_between(start_date=datetime(2022, 1, 1, 0, 0, 1))
            customers.append(
                {
                    "model": "Customer.customer",
                    "pk": self.pk,
                    "fields": {
                        "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(90),
                        "first_name": self.sex_dict[self.sex]['first_name'](),
                        "last_name": self.sex_dict[self.sex]['last_name'](),
                        "patronymic": self.sex_dict[self.sex]['middle_name'](),
                        "sex": self.sex,
                        "email": self.fake.email(),
                        "phone_number": self.fake.phone_number(),
                        "country": self.fake.country_code(),
                        "balance": str(self.fake.pydecimal(min_value=0, max_value=200_000, right_digits=2))
                    }
                }
            )
            self.pk += 1
        return customers
