from django.contrib import admin
from .models import KZzone, RUSzone, Tariff

admin.site.register(KZzone)
admin.site.register(RUSzone)
admin.site.register(TariffFromKZtoRUS)
admin.site.register(Calculator)

# Register your models here.
