from django.urls import path
from .views import HomePageView,AboutPageView 

app_name = 'pages'

urlpatterns = [

	path('pages/homepage', HomePageView.as_view(), name='home'),
	path('pages/aboutpage', AboutPageView.as_view(), name='about') 

]