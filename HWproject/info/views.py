from django.shortcuts import render

from info.models import *


def main_page(request):
    return render(request, 'index.html', {'texts': Description.objects.all()})


def demand_page(request):
    return render(request, 'demand.html', {'demand_graphs': DemandGraph.objects.all()})


def geography_page(request):
    return render(request, 'geography.html', {'geography_graphs': GeographyGraph.objects.all()})


def skills_page(request):
    return render(request, 'skills.html', {'skills_graphs': SkillsGraph.objects.all()})


def last_vacancies_page(request):
    return render(request, 'lastvacancies.html', {'last_vacancies': LastVacancy.objects.all()})
