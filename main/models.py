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


class About(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.name


class Performance(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    experience = models.CharField(max_length=2, verbose_name='Опыт')
    projects = models.CharField(max_length=3, verbose_name='Количество проектов')
    models = models.CharField(max_length=3, verbose_name='Количество моделей')

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название проекта')
    image = models.ImageField(upload_to='projects/', verbose_name='Фото проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Реализованные проекты'

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    position = models.CharField(max_length=50, verbose_name='Позиция/должность')
    text = models.TextField(verbose_name='Текст отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование банка')
    logo = models.ImageField(upload_to='bank/', verbose_name='Лого банка')

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

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


class Order(models.Model):
    customer = models.CharField(max_length=250, verbose_name='Имя заказчика')
    theme = models.CharField(max_length=150, blank=True, verbose_name='Тема')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки заказчиков'

    def __str__(self):
        return self.customer


