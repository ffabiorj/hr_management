from django.contrib.auth.models import User
from departaments.models import Departament
from companies.models import Company
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departament = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
