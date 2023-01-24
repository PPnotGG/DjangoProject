import re
import requests
from django.shortcuts import render
from .models import *


def main_page(request):
    main_info = Description.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'main_info': main_info}
    return render(request, 'index.html', context)


def demand_page(request):
    demand_info = DemandGraph.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'demand_info': demand_info}
    return render(request, 'demand.html', context)


def geography_page(request):
    geography_info = GeographyGraph.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'geography_info': geography_info}
    return render(request, 'geography.html', context)


def skills_page(request):
    skills_info = SkillsGraph.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'skills_info': skills_info}
    return render(request, 'skills.html', context)


def last_vacancies_page(request):

    class HHAPI:

        def __init__(self, search_text: str):
            self.text = search_text

        def __get_full_vacancies__(self, date: str, count_vac: int) -> list:
            url = 'https://api.hh.ru/vacancies'
            return requests.get(url, dict(text=self.text,
                                          specialization=1,
                                          date_from=f"{date}T00:00:00",
                                          date_to=f"{date}T23:00:00",
                                          per_page=count_vac,
                                          page=1)).json()["items"]

        def get_data_vacancies(self, date: str, count_vac: int):
            data = self.__get_full_vacancies__(date, count_vac)
            result_list = []
            for vac in data:
                url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
                resp = requests.get(url_vac).json()
                if resp['salary']:
                    description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                                           .strip()
                                           .split())
                    description = description[:100] + '...' if len(description) >= 100 else description
                    result_list.append({'name': resp['name'],
                                        'description': description,
                                        'key_skills': list(map(lambda x: x['name'], resp['key_skills'])),
                                        'employer': resp['employer']['name'],
                                        'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                                        'area': resp['area']['name'],
                                        'published_at': resp['published_at'][:10],
                                        'alternate_url': resp['alternate_url']})

            return result_list

    hh = HHAPI('C++')
    vacs = hh.get_data_vacancies('2022-12-26', 10)

    last_vacancies = LastVacancy.objects.all()
    navigation = Navigation.objects.all()
    context = {'vacs': vacs, 'last_vacancies': last_vacancies, 'navigation': navigation}
    return render(request, 'lastvacancies.html', context)
