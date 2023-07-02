from django.urls import path
from .forms import UserLoginForm
from . import views
from django.contrib.auth import views as def_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('sign-up/', views.register_view, name='user-register'),
    path(
        'login/',
        views.login_view,
        name='user-login'
    ),
    path(
        'account-reset/',
        views.account_reset_view,
        name='user-reset'
    ),
    path(
        'logout/',
        view=views.logout_user,
        name='logout',
    ),
    
    path(
        'my-account',
        view=views.user_account_view,
        name='user-account',
    ),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
