from django.shortcuts import render
from django.core.mail import  send_mail
from django.conf import settings


def email_list(request):
    subject = request.POST.get('msg')
    if request.method == ['POST']:
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')

        # email = EmailMessage(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [receiver]
        # )
        # email.fail_silently = True
        # email.send()
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [receiver],
            fail_silently=False
        )

    return render(request, 'sender.html', {'subject': subject})
