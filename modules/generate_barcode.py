import random as rnd
import barcode
from barcode.writer import ImageWriter
import os

output_dir = "barcode"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def create(nama):
    id = ""

    for i in range(13):
        random_number = rnd.randint(0, 9)
        random_numbers_str = str(random_number)
        id = id + random_numbers_str

    id_int = int(id)

    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(str(id_int).zfill(12), writer=ImageWriter())
    filename = f'tiket barcode {nama}'
    full_path = os.path.join(output_dir, filename)
    ean.save(full_path)
    return id_int
