from django.urls import path

from .views import BlogListView, BlogDetailedView

urlpatterns = [
	path('homepage/', BlogListView.as_view(), name='home'),
	path('post/<int:pk>', BlogDetailedView.as_view(), name='detail_view'),
]
