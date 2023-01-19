from django.db import models


class Navigation(models.Model):
    logo_field = models.ImageField(upload_to='media/', blank=False, verbose_name='Логотип')
    first_menu = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=50)
    second_menu = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=50)
    third_menu = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=50)
    fourth_menu = models.TextField(blank=False, verbose_name='Четвертый пункт меню',max_length=50)
    fifth_menu = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=50)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)


class Description(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', blank=False, verbose_name='Фото')


class DemandGraph(models.Model):
    content = models.TextField(blank=True, verbose_name='Таблицы')
    graph1 = models.ImageField(upload_to='media/', blank=False, verbose_name='Первый график сравнения')
    graph2 = models.ImageField(upload_to='media/', blank=False, verbose_name='Второй график сравнения')


class GeographyGraph(models.Model):
    content = models.TextField(blank=True, verbose_name='Таблицы')
    first_header = models.CharField(max_length=100, blank=True, verbose_name='Заголовок для первого фото')
    graph1 = models.ImageField(upload_to='media/', blank=False, verbose_name='Первый график')
    second_header = models.CharField(max_length=100, blank=True, verbose_name='Заголовок для второго фото')
    graph2 = models.ImageField(upload_to='media/', blank=False, verbose_name='Второй график')


class SkillsGraph(models.Model):
    header = models.CharField(max_length=100, blank=True, verbose_name='Заголовок для таблицы')
    content = models.TextField(blank=True, verbose_name='Таблица')
    graph = models.ImageField(upload_to='media/', blank=False, verbose_name='График')


class LastVacancy(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
