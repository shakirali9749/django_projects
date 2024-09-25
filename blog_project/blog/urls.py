from django.urls import path

from .views import (
	BlogListView,
	BlogDetailView,
	BlogCreateView,
	BlogUpdateView, # new
	BlogDeleteView,
)

urlpatterns = [
	
	path('post/<int:pk>/delete',BlogDeleteView.as_view(), name='post_delete'),
	path('homepage/', BlogListView.as_view(), name='home'),
	path('post/<int:pk>', BlogDetailView.as_view(), name='detail_view'),
	path('post/new/', BlogCreateView.as_view(), name='post_new'),
	path('post/<int:pk>/edit',BlogUpdateView.as_view(), name='post_edit'),

]
