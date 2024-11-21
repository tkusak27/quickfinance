# example/urls.py
from django.urls import path

from quickfinance.views import index, skills


urlpatterns = [
    path('/', index, name='index'),
    path('skills/', skills, name='skills')
]