import qrcode

#Here you can change every product name and code, they are here set just for a exemple for you understand how the code work in a qr_code list#

information_link ={
    "Portifólio": "",
    "GitHub": "https://github.com/victorgabrielnascimento",
    "Linkedin": "https://www.linkedin.com/in/victorgnascimento/"
}

for information in information_link:
    link = information_link[information]
    qrcode_image = qrcode.make(link)
    qrcode_image.save(f"qrcode_{information}.png")
