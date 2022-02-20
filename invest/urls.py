from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from main.views import IndexView, ArticlesList, ArticleDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
