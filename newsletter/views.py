from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from .models import Subscriber
from .forms import SubcriberForm, NewsletterForm

# Create your views here.

def subscriber(request):
    success = False

    if request.method == 'POST':
        form = SubcriberForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = SubcriberForm()

    return render(request, 'subscriber.html', {'form': form, 'success': success})

@staff_member_required
def send_newsletter(request):
    success = False

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            subscribers = Subscriber.objects.values_list('email', flat=True)

            messages = [
                (subject, message, None, [email])
                for email in subscribers
            ]

            send_mass_mail(messages, fail_silently=False)
            success = True
            form = NewsletterForm()
    else:
            form = NewsletterForm()

    return render(request, 'send_newsletter.html', {'form': form, 'success': success})