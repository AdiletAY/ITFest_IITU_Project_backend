
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(
    to_email: str, context: object, html_template_path: str, subject: str, message: str
):
    msg = render_to_string(html_template_path, context)

    send_mail(
        subject=subject,
        message=message,
        html_message=msg,
        from_email="noreply@university.edu.kz",
        recipient_list=[to_email],
    )
