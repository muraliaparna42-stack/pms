from django.urls import path
from .views import home,export_csv
urlpatterns=[
    path('',home,name='home'),
    path('export/',export_csv,name='export_csv'),
]