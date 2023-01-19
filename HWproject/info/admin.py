from django.contrib import admin
from .models import Description, DemandGraph, GeographyGraph, SkillsGraph, LastVacancy, Navigation

admin.site.register(Navigation)
admin.site.register(Description)
admin.site.register(DemandGraph)
admin.site.register(GeographyGraph)
admin.site.register(SkillsGraph)
admin.site.register(LastVacancy)
