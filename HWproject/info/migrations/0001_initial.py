# Generated by Django 4.1.5 on 2023-01-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemandGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Таблицы')),
                ('graph1', models.ImageField(upload_to='media/', verbose_name='Первый график сравнения')),
                ('graph2', models.ImageField(upload_to='media/', verbose_name='Второй график сравнения')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='GeographyGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Таблицы')),
                ('first_header', models.CharField(blank=True, max_length=100, verbose_name='Заголовок для первого фото')),
                ('graph1', models.ImageField(upload_to='media/', verbose_name='Первый график')),
                ('second_header', models.CharField(blank=True, max_length=100, verbose_name='Заголовок для второго фото')),
                ('graph2', models.ImageField(upload_to='media/', verbose_name='Второй график')),
            ],
        ),
        migrations.CreateModel(
            name='LastVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_field', models.ImageField(upload_to='media/', verbose_name='Логотип')),
                ('first_menu', models.TextField(max_length=50, verbose_name='Первый пункт меню')),
                ('second_menu', models.TextField(max_length=50, verbose_name='Второй пункт меню')),
                ('third_menu', models.TextField(max_length=50, verbose_name='Третий пункт меню')),
                ('fourth_menu', models.TextField(max_length=50, verbose_name='Четвертый пункт меню')),
                ('fifth_menu', models.TextField(max_length=50, verbose_name='Пятый пункт меню')),
                ('author', models.TextField(max_length=50, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=100, verbose_name='Заголовок для таблицы')),
                ('content', models.TextField(blank=True, verbose_name='Таблица')),
                ('graph', models.ImageField(upload_to='media/', verbose_name='График')),
            ],
        ),
    ]
