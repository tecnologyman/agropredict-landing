from django.urls import path
from .views import home, legal

urlpatterns = [
    path('', home, name='home'),
    path('legal/', legal, name='legal'),
]
