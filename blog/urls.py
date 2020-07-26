from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView, 
	UserPostListView,
	) 


urlpatterns = [
	#path('home/',views.home, name='blog-home'),
	path('about/',views.about, name='blog-about'),
	path('home/', PostListView.as_view(), name='blog-home'), # for class based views
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # class based view
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # check: is the author of the post trying to acess the page???
	path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts')

]


# <app_name>/<model_name>_<viewtype>.html