from django.contrib import admin
admin.site.site_header = "Riwan moble Shope"
admin.site.index_title = "Welcome to Riwan Moble Shope"
admin.site.site_title = "Asif Tutorial"
# Register your models here.
from .models import *
admin.site.register(Contact)
