import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def generate_code():
    return "".join(random.choice("0123456789") for i in range(5))


def send_email_verification_code(data):
    context = {
        "email_body": f"Hi {data['name']}, \n Use the code below to verify your email for your KtechHub Account to be activated.",
        "verify_code": data["verify_code"],
        "email": data["email"],
        "name": data["name"],
        "subject": "DRF - Account Activation",
    }

    mail_template = get_template("email/verify_email.html").render(context)

    email = EmailMultiAlternatives(
        subject=context["subject"], body=" ", to=[context["email"]]
    )
    email.attach_alternative(mail_template, "text/html")
    email.send()
