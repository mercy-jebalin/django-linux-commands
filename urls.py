from . import views
from django.urls import path

urlpatterns = [
path('', views.home,name="home-page"),
path('sec',views.sec,name='sec'),
path('help',views.help,name='help'),
path('home',views.home,name='home-page'),
path('about',views.about,name='about'),
path('contact',views.contact,name='contact'),
path('db',views.db,name='thank')
]
