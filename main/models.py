from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование статьи')
    image = models.ImageField(upload_to='article/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Slider(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название слайда')
    image = models.ImageField(upload_to='slides', verbose_name='Изображение слайда')
    description = models.TextField(verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название контакта')
    phone = models.CharField(max_length=18, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    facebook = models.URLField(verbose_name='Страница в фейсбуке')
    vk = models.URLField(verbose_name='Страница В Контакте')
    instagram = models.URLField(verbose_name='Страница в Инстаграме')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class OrderForm(models.Model):
    customer = models.CharField(max_length=250, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    organization = models.CharField(max_length=200, blank=True, verbose_name='Организация')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки заказчиков'

    def __str__(self):
        return self.customer


