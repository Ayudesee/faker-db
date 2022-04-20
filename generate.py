from CustomerGenerator.CustomerGenerator import CustomerGenerator
from DealerGenerator.DealerGenerator import DealerGenerator
from SupplierGenerator.SupplierGenerator import SupplierGenerator
from CarGenerator.CarGenerator import CarGenerator
from AdGenerator.AdGenerator import DealerAdGenerator, SupplierAdGenerator
from GarageGenerator.GarageGenerator import DealerGarageGenerator, SupplierGarageGenerator
import json
import re


cg = CustomerGenerator()
dg = DealerGenerator()
sg = SupplierGenerator()
carg = CarGenerator()
dadg = DealerAdGenerator()
sadg = SupplierAdGenerator()
dgg = DealerGarageGenerator()
sgg = SupplierGarageGenerator()

data = []
data.extend(cg.generate(150, "M"))
data.extend(cg.generate(50, "F"))
data.extend(dg.generate(100))
data.extend(sg.generate(100))
data.extend(carg.generate(150))
data.extend(dadg.generate(50))
data.extend(sadg.generate(50))
data.extend(dgg.generate(25, 90))
data.extend(sgg.generate(30, 70))

with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file)


