from datetime import datetime

import numpy as np
from faker import Faker


class LoginUserGenerator:
    def __init__(self):
        self.fake = Faker('ru-RU')
        self.user_type = ("C", "D", "S")
        self.user_type_weights = (0.7, 0.2, 0.1)
        self.pk = 1

    def generate(self, amount=10):
        users = []

        for i in range(amount):
            while True:
                email = self.fake.email()
                username = self.fake.profile()['username']
                for user in users:
                    if email == user['fields']['email'] or username == user['fields']['username']:
                        continue
                break
            time = self.fake.date_time_between(
                start_date=datetime(2022, 4, 4, 1, 1, 1),
                end_date=datetime(2022, 5, 1, 1, 1, 1)
            )
            users.append(
                {
                    "model": "LoginUser.loginuser",
                    "pk": self.pk,
                    "fields": {
                        "password": "pbkdf2_sha256$260000$TTiLzQzxxB1KpqeI5kknOG$Nj/NNgigwiKF+Am77+XzbtDeqYi06Z5/Z11qp7FfZIY=",
                        "last_login": "2022-04-29T12:47:20.600Z",
                        "is_superuser": False,
                        "username": username,
                        "first_name": "",
                        "last_name": "",
                        "is_staff": False,
                        "date_joined": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
                        "is_active": self.fake.boolean(95),
                        "email": email,
                        "user_type": np.random.choice(self.user_type, p=self.user_type_weights),
                        "groups": [],
                        "user_permissions": []
                    }
                }
            )
            self.pk += 1
        return users


if __name__ == '__main__':
    ug = LoginUserGenerator()
    d = ug.generate(10)
    for i in d:
        print(i)
