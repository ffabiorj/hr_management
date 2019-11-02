from django.views.generic.edit import CreateView
from .models import Company


class CreateCompany(CreateView):
    model = Company



