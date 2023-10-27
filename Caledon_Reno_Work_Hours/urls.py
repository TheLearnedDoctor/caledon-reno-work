from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('apply/', views.apply, name='apply'),
    # path('', views.homepage, name='home'),
    path('estimate/', views.estimate, name='estimate'),
    path('', views.home, name='work_hours_home'),
    path('import/', views.import_from_excel, name='import_from_excel'),

]