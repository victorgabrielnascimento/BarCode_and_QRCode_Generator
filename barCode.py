from barcode import EAN13
from barcode.writer import ImageWriter

#Here you can change every product name and code, they are here set just for a exemple for you understand how the code work in a bar_code list#

product_code ={
    "Xbox-Series-XS": "551746511312",
    "Iphone-14-Pro": "192837462536",
    "NoteBook-Samsung-i5": "192756381921",
    "Wash-Machine": "839102938457",
    "Refrigerator": "223940187623"
}

for product in product_code:
    code = product_code[product]
    bar_code = EAN13 (code, writer=ImageWriter())
    bar_code.save(f"{product}_bar_code")