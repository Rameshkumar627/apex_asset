from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    manager = models.ForeignKey("Employee", related_name="employee_name",
                                blank=True, null=True,
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department")
    email = models.EmailField(max_length=254, verbose_name="Email", null=True)
    dob = models.DateField(verbose_name="DOB", null=True)

    def __str__(self):
        return self.name
