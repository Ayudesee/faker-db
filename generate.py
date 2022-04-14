from CustomerGenerator.CustomerGenerator import CustomerGenerator
from DealerGenerator.DealerGenerator import DealerGenerator
from SupplierGenerator.SupplierGenerator import SupplierGenerator
from CarGenerator.CarGenerator import CarGenerator


cg = CustomerGenerator()
print(cg.generate(10, "F"))
print(cg.generate(5, "M"))
dg = DealerGenerator()
print(dg.generate(20))
sg = SupplierGenerator()
print(sg.generate(5))
carg = CarGenerator()
print(carg.generate(1))
