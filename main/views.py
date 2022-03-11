from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django import views
from django.contrib import messages
from .forms import *
from .models import *


def index(request):
    title = 'fff'
    description = 'ffff'
    projects = Project.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            Order = form.save(commit=False)
            cd = form.cleaned_data
            Order.save()
            messages.success(request, 'Ваше сообщение отправленно. Мы рассмотрим его в самое ближайшее время.')
            messages.error(request, 'Ошибка.')
            subject = 'Сообщение от {} ({})'.format(cd['customer'], cd['email'])
            message = '"{}". {} | {}'.format(cd['comment'], cd['customer'], cd['phone'])
            send_mail(subject, message, 'form@invest.ru', [cd['email'], 'checkago@yandex.ru'])
            return redirect('/#model')

    else:
        form = OrderForm()

    return render(request, 'index.html', {'form': form, 'title': title, 'description': description,
                                          'projects': projects})


class ArticlesList(views.View):

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'articles.html', context)


class ArticleDetail(views.generic.DetailView):
    model = Article

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'article_detail.html', context)

