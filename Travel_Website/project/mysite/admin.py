from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fields = ('username','password')
    list_display = ('username','password')
    ordering = ['username']

class ReviewAdmin(admin.ModelAdmin):
    fields = ('country','title', 'country_review')
    list_display = ('country','title')
    ordering = ['country']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)
