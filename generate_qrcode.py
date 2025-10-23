import random as rnd
import barcode
from barcode.writer import ImageWriter

id = ""

for i in range(13):
    random_number = rnd.randint(0, 9)
    random_numbers_str = str(random_number)
    id = id + random_numbers_str
    print(id)

id_int = int(id)

print(id_int)
EAN = barcode.get_barcode_class('ean13')
ean = EAN(str(id_int).zfill(12), writer=ImageWriter())
filename = ean.save('ean13_barcode')
