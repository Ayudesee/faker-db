from faker import Faker
from faker_vehicle import VehicleProvider
from random import randint
from datetime import datetime
import numpy as np
from CustomerGenerator.CustomerGenerator import CustomerGenerator

# {"model": "Customer.customer", "pk": 3, "fields": {"created_at": "2022-04-08T10:04:43.363Z", "updated_at": "2022-04-08T10:04:43.363Z", "is_active": true, "first_name": "Мария", "last_name": "Петрова", "patronymic": "Геннадьевна", "sex": "F", "phone_number": "8029646464", "country": "BB", "balance": "0.00"}}

# fake = Faker('ru-RU')
# fake.add_provider(VehicleProvider)
# print(fake.vehicle_year_make_model())
print()
# print(fake.first_name_male())
# print(fake.last_name_male())
# print(fake.middle_name_male())
# print(fake.country_code())
# print(fake.boolean(90))
# print(fake.email())
# print(fake.city())
# print(fake.street_address())
# print("M")
# print(fake.phone_number())
# time = fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 24, 38))
# print(f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z")
# print(type(fake.pydecimal(min_value=0, max_value=200_000, right_digits=2)))

# persons_male = {}
# for i in range(10):
#     time = fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 24, 38))
#     persons_male[i + 1] = {
#         "model": "Customer.customer",
#         "pk": i + 1,
#         "fields": {
#             "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "is_active": fake.boolean(90),
#             "first_name": fake.first_name_male(),
#             "last_name": fake.last_name_male(),
#             "patronymic": fake.middle_name_male(),
#             "sex": "M",
#             "phone_number": fake.phone_number(),
#             "country": fake.country_code(),
#             "balance": fake.pydecimal(min_value=0, max_value=200_000, right_digits=2)
#         }
#     }
#
# for obj in persons_male.items():
#     print(obj)
#
#
# dealers = {}
# for i in range(10):
#     time = fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 24, 38))
#     dealers[i + 1] = {
#         "model": "Dealer.dealer",
#         "pk": i + 1,
#         "fields": {
#             "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "is_active": fake.boolean(95),
#             "name": fake.company(),
#             "country": fake.country_code(),
#             "location": f"{fake.city()} {fake.street_address()}",
#             "balance": fake.pydecimal(min_value=200_000, max_value=5_200_000, right_digits=2)
#         }
#     }
# for obj in dealers.items():
#     print(obj)
#
# suppliers = {}
# for i in range(10):
#     time = fake.date_time_between(start_date=datetime(2022, 1, 1, 1, 24, 38))
#     suppliers[i + 1] = {
#         "model": "Supplier.supplier",
#         "pk": i + 1,
#         "fields": {
#             "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "is_active": fake.boolean(95),
#             "name": f"{fake.company()} {fake.company_suffix()}",
#             "country": fake.country_code(),
#             "location": f"{fake.city()} {fake.street_address()}",
#             "foundation_year": randint(1890, 1960)
#         }
#     }
#
# for obj in suppliers.items():
#     print(obj)

# vbrand = ["Audi", "Mercedes", "Nissan", "Mazda", "Lada", "UAZ", "Porsche", "Ferrari", "Lamborghini", "Honda", "Hyundai",
#           "Geely", "Skoda", "Volkswagen", "Ford", "Kia", "Renault", "Toyota", "Tesla", "Opel", "Daewoo", "Citroen"]
# vmodel = ["Patriot"]
# vtype = ["station wagon", "sedan", "coupe", "hatchback", "minivan"]
# vtransmission = ["Manual", "Automatic"]
# vtransmission_weights = [0.4, 0.6]
# vtod = ["Front", "Rear", "Full"]
# vtod_weights = [0.15, 0.75, 0.1]
# cars = {}
# print()
# for i in range(10):
#     car = fake.vehicle_object()
#     time = fake.date_time_between(start_date=datetime(2022, 1, 1, 0, 0, 0))
#     cars[i + 1] = {
#         "model": "Utility.car",
#         "pk": i + 1,
#         "fields": {
#             "created_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "updated_at": f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}.123Z",
#             "is_active": fake.boolean(95),
#             "brand": car['Make'],
#             "model": car['Model'],
#             "year": car['Year'],
#             "description": {
#                 "type": car['Category'],
#                 "mass": randint(800, 1600),
#                 "transmission": np.random.choice(vtransmission, p=vtransmission_weights),
#                 "Type of drive": np.random.choice(vtod, p=vtod_weights),
#                 "Fuel tank capacity": randint(45, 100)
#             }
#         }
#     }
#
# for obj in cars.items():
#     print(obj)


cg = CustomerGenerator()
print(cg.generate(10, "F"))
print(cg.generate(5, "M"))
