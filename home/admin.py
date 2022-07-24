from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Userprofile)
admin.site.register(Skill)
admin.site.register(Services)
admin.site.register(Portfolios)
admin.site.register(Tags)
admin.site.register(ContactForm)
admin.site.register(Achievements)









