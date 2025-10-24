import random as rnd
import barcode
from barcode.writer import ImageWriter


def create():
    id = ""

    for i in range(13):
        random_number = rnd.randint(0, 9)
        random_numbers_str = str(random_number)
        id = id + random_numbers_str

    id_int = int(id)

    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(str(id_int).zfill(12), writer=ImageWriter())
    filename = ean.save('ean13_barcode')
    return id_int
