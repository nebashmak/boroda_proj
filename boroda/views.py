from django.contrib import auth
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from boroda.models import Product
from boroda_proj.forms import ContactForm






def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():

            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            phone = form.cleaned_data['phone']

            recepients = ['borodaa@gmail.com']

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)


            try:
                send_mail(phone, message, 'borodaa@gmail.com', recepients)

            except BadHeaderError: # Защита от уязвимости
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect('/thanks.html')

    else:
        form = ContactForm()


    return render(reguest, 'boroda/contact.html', {'form': form, 'username': auth.get_user(reguest).username})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'boroda/thanks.html', {'thanks': thanks})

def base(request):
    return render(request, 'boroda/base.html')

def tovari(request):
    return render(request, 'boroda/tovari.html')

def male(request):
    name = Product.objects.get(id=3)

    context = {
        'name': name
    }
    return render(request, 'boroda/male.html', context)

def female(request):
    name = Product.objects.get(id=1)

    context={
        'name': name
    }
    return render(request, 'boroda/female.html', context)

def kids(request):
    name = Product.objects.get(id=4)

    context = {
        'name': name
    }
    return render(request, 'boroda/kids.html', context)


