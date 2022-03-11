from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название проекта')
    image = models.ImageField(upload_to='projects/', verbose_name='Фото проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Реализованные проекты'

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя заказчика')
    theme = models.CharField(max_length=150, blank=True, verbose_name='Тема')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, verbose_name='Электронная почта')
    text = models.TextField(blank=True, verbose_name='Текст')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки заказчиков'

    def __str__(self):
        return self.name


