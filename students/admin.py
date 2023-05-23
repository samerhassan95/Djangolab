from django.contrib import admin
from .models import Student, Staff


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city', 'supervisor')
    list_filter = ('supervisor',)
    search_fields = ('name', 'city')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')
    search_fields = ('name', 'position', 'email', 'phone')
# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)