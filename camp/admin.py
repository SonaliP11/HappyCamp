from django.contrib import admin
from .models import Club
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.




class ClubAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'location', 'age_group_min', 'age_group_max', 'start_date', 'end_date', 'is_active', 'status')
    list_filter = ('is_active', 'status')
    search_fields = ('name',  'location')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'daily_schedule')

# Register your models here.
admin.site.register(Club, ClubAdmin)