# function base view
# from django.shortcuts import render

# # Create your views here.

# def homePageView(request):

# 	return render(request, 'pages/index.html')


# classbase view

from django.views.generic import TemplateView
# from django.views import
class HomePageView(TemplateView):

	template_name = 'pages/home.html'

class AboutPageView(TemplateView):

	template_name = 'pages/about.html'