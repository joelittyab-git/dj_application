from . import views
from django.urls import path, include

urlpatterns = [
   path('', views.home_view, name='blog-home'), 
   path('post/', views.post_blog_view, name='blog-post'),
   path('user/', include('user.urls'))
]
