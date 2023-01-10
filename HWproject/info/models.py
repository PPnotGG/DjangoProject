from django.db import models


class Description(models.Model):
    header = models.CharField(max_length=255)
    text = models.CharField(max_length=2048)
    image = models.ImageField(upload_to='info/static/img', height_field=None, width_field=None, max_length=100, default='')
    IMAGE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    check_image = models.CharField(choices=IMAGE_CHOICES, max_length=255, default='')


class DemandGraph(models.Model):
    header = models.CharField(max_length=255)
    image = models.ImageField(upload_to='info/static/img', height_field=None, width_field=None, max_length=100, default='')


class GeographyGraph(models.Model):
    header = models.CharField(max_length=255)
    image = models.ImageField(upload_to='info/static/img', height_field=None, width_field=None, max_length=100, default='')


class SkillsGraph(models.Model):
    header = models.CharField(max_length=255)
    image = models.ImageField(upload_to='info/static/img', height_field=None, width_field=None, max_length=100, default='')


class LastVacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    region = models.CharField(max_length=255)
    date = models.DateField()
