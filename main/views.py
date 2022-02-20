from django.shortcuts import render
from django import views
from django.views.generic import DetailView

from main.models import Article, Slider, Contact


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.all()
        contact = Contact.objects.last()
        context = {
            'sliders': sliders,
            'contact': contact,
        }
        return render(request, 'index.html', context)


class ArticlesList(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'articles.html', context)


class ArticleDetail(views.generic.DetailView):
    model = Article

    def get(self, request, *args, **kwargs):
        return render(request, 'article_detail.html', context)

