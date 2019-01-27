
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from application.views import *
from django.urls import include
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from user_account import views as user_account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^application/', include('application.urls')),
    url(r'^signup/', user_account_views.signup, name='signup'),
    url(r'^login/', auth_views.LoginView.as_view(
        template_name='user_account/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(
        template_name='user_account/logout.html'), name='logout'),
    path('profile/', user_account_views.profile, name='profile'),
    url('editprofile', user_account_views.edit_profile, name = 'edit-profile'),
    path('', RedirectView.as_view(url='/application/', permanent=True)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)