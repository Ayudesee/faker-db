from CustomerGenerator.CustomerGenerator import CustomerGenerator
from DealerGenerator.DealerGenerator import DealerGenerator
from SupplierGenerator.SupplierGenerator import SupplierGenerator
from CarGenerator.CarGenerator import CarGenerator
from AdGenerator.AdGenerator import DealerAdGenerator, SupplierAdGenerator
from GarageGenerator.GarageGenerator import DealerGarageGenerator, SupplierGarageGenerator
from UserGenerator.UserGenerator import LoginUserGenerator
from random import choice
import json
import re

ug = LoginUserGenerator()
cg = CustomerGenerator()
dg = DealerGenerator()
sg = SupplierGenerator()
carg = CarGenerator()
dadg = DealerAdGenerator()
sadg = SupplierAdGenerator()
dgg = DealerGarageGenerator()
sgg = SupplierGarageGenerator()

data = []


users = ug.generate(1000)
customers = []
dealers = []
suppliers = []

for user in users:
    if user['fields']['user_type'] == "C":
        if user['pk'] % 2 == 0:
            customers.extend(cg.generate(user_id=user['pk'], amount=1, gender="M"))
        else:
            customers.extend(cg.generate(user_id=user['pk'], amount=1, gender="F"))
    elif user['fields']['user_type'] == "D":
        dealers.extend(dg.generate(user_id=user['pk'], amount=1))
    elif user['fields']['user_type'] == "S":
        suppliers.extend(sg.generate(user_id=user['pk'], amount=1))

d_gars = []
d_ads = []
s_gars = []
s_ads = []
for dealer in dealers:
    d_gars.extend(dgg.generate(25, dealer['pk'], 1))
    d_ads.extend(dadg.generate(dealer_id=dealer['pk'], ads_amount=10))
for supplier in suppliers:
    s_gars.extend(sgg.generate(25, supplier['pk'], 1))
    s_ads.extend(sadg.generate(supplier_id=supplier['pk'], dealer_id=choice(dealers)['pk'], ads_amount=5))


data.extend(users)
data.extend(customers)
data.extend(dealers)
data.extend(suppliers)
data.extend(carg.generate(100))
data.extend(d_gars)
data.extend(s_gars)
data.extend(d_ads)
data.extend(s_ads)

with open('data45.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file)


