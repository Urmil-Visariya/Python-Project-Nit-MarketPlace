from django.core.mail import EmailMessage

def send_requested_product(value):
    img_name=value.pic.name.removeprefix("requsted_pictures/")
    email = EmailMessage("req product", f"{value.name}\n{value.desc}", "checkmailproject84@gmail.com", ["advaitbhavin@gmail.com"])
    email.attach(img_name,value.pic.read(),"image/png")
    email.send()