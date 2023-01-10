from django.db import models


class Description(models.Model):
    header = models.CharField(max_length=255)
    text = models.CharField(max_length=2048)
    image = models.CharField(max_length=255, default='')


class DemandGraph(models.Model):
    header = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class GeographyGraph(models.Model):
    header = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class SkillsGraph(models.Model):
    header = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class LastVacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    region = models.CharField(max_length=255)
    date = models.DateField()
