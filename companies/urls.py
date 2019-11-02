from django.urls import path
from .views import CreateCompany

urlpatterns = [
    path('novo', CreateCompany.as_view(), name='create_company'),
]