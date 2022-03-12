from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django import views
from django.contrib import messages
from main.forms import OrderForm
from main.models import Project


def index(request):
    title = 'fff'
    description = 'ffff'
    projects = Project.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            new_order = form.save(commit=False)
            cd = form.cleaned_data
            new_order.save()
            messages.success(request, 'Ваша сообщение успешно отправлено!')
            subject = 'Сообщение от {} ({})'.format(cd['name'], cd['email'])
            message = '"{}". {} | {}'.format(cd['text'], cd['name'], cd['phone'])
            send_mail(subject, message, 'invest-consult1@yandex.ru', [cd['email'], 'irina.palitsyna@gmail.com'])
            sent = True
            return redirect('/')

    else:
        form = OrderForm()

    return render(request, 'index.html', {'form': form, 'title': title, 'projects': projects, 'description': description})

