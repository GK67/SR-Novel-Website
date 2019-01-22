from django.conf.urls import url
#from django.conf.urls import include
#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='index'),
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signup/$', views.signup, name = 'signup'),
	#path('login/', views.LoginView.as_view(), name='login'),
    #path('index/', index, name = 'index'),
    #path('signup/',SignUpView.as_view(),name='signup'),

    #url(r'^$', views.index, name='index'),
     #url(r'^(?P<playlist-id>\d/+)$', views.index, name='select_playlist'),
     
]

'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
]'''