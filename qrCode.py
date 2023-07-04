import qrcode

information_link ={
    "Portifólio": "",
    "GitHub": "https://github.com/victorgabrielnascimento",
    "Linkedin": "https://www.linkedin.com/in/victorgnascimento/"
}

for information in information_link:
    link = information_link[information]
    qrcode_image = qrcode.make(link)
    qrcode_image.save(f"qrcode_{information}.png")
