from django.urls import path
from . import views

# importing a Django function called path.
# Importing everything from views.

urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
]

# '' is resolved as localhost.
# we're now assigning a view called post_list to the root URL
# The last part, name='post_list', is the name of the URL that will be used to identify the view. ?
