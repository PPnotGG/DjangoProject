from django.shortcuts import render


def main_page(request):
    return render(request, 'index.html')


def geography_page(request):
    return render(request, 'geography.html')


def demand_page(request):
    return render(request, 'demand.html')


def skills_page(request):
    return render(request, 'skills.html')


def last_vacancies_page(request):
    return render(request, 'lastvacancies.html')
