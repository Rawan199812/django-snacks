from .views import HomePageView
from .views import AboutPageView

from django.urls import path
urlpatterns = [
    path('', HomePageView.as_view(),name = "home"), # we use as_views because HomePageView is class 
    path('about', AboutPageView.as_view(),name = "about"),

]
