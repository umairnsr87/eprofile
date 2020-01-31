
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('create-resume', views.create_resume,name='create-resume'),

    path('details/',views.details,name='details'),
]
