from django.contrib import admin
from .models import Employee, Department
from django.contrib.admin import DateFieldListFilter


class EmployeeTabularInline(admin.TabularInline):
    model = Employee


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeTabularInline]
    list_display = ('name', 'manager')
    search_fields = ['name', 'manager']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'email', 'dob')
    list_filter = (
        ('dob', DateFieldListFilter),
        'department'
    )
    search_fields = ['department', 'dob']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
