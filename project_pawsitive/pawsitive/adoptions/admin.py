from django.contrib import admin
from .models import Donation, Adoption, Volunteer ,PreAdoption

admin.site.register(Donation)
admin.site.register(Adoption)
admin.site.register(Volunteer)
admin.site.register(PreAdoption)
