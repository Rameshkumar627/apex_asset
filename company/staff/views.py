from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Department, Employee
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'department'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        departments = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(departments, self.paginate_by)
        try:
            departments = paginator.page(page)
        except PageNotAnInteger:
            departments = paginator.page(1)
        except EmptyPage:
            departments = paginator.page(paginator.num_pages)
        context['departments'] = departments
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context


class EmployeeDetailView(DetailView):

    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'


@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_create.html'
    fields = ('name', 'department', )
    success_url = reverse_lazy('employee-list')
