from django.conf.urls import url
from django.conf.urls import include
#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView


urlpatterns = [

	path('', views.index, name='index'),
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signup/$', views.signup, name = 'signup'),
	url(r'^forget/$', views.forget_v, name = 'forget_u'),

	url(r'^password-reset/$', 
		auth_views.PasswordResetView.as_view(
		template_name='templates/registration/password_reset.html'),
		name='password_reset'),
	url(r'^password-reset/done/$', 
		auth_views.PasswordResetDoneView.as_view(
		template_name='templates/registration/password_reset_done.html'),
		name='password_reset_done'),
    
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
        	template_name= 'templates/registration/password_reset_confirm.html'),
        	name='password_reset_confirm'),

    url(r'^password-reset-complete/$', 
		auth_views.PasswordResetCompleteView.as_view(
		template_name='templates/registration/password_reset_complete.html'),
		name='password_reset_complete'),
	#path('login/', views.LoginView.as_view(), name='login'),
	# url(r'^profile/$',views.profile,name = 'profile'),
	url('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
	url('editprofile', views.edit_profile, name = 'edit-profile'),
	url('logout', views.logout_view, name = 'logout'),
	url('uploadbook',views.upload_book,name = 'upload-book'),

	path('books/', BookListView.as_view(),name='booklist'),
	path('book/<int:pk>/', BookDetailView.as_view(),name='book-detail'),
	path('book/<int:pk>/update', BookUpdateView.as_view(),name='book-update'),
	path('book/create_book/', BookCreateView.as_view(),name='book-create'),
	path('book/<int:pk>/book-content',views.BookContentView.as_view(),name='book-content'),
	# url(r'^profile/editProfile/$',views.editProfileView.as_view(),name='editProfile'),

    #path('index/', index, name = 'index'),
    #path('signup/',SignUpView.as_view(),name='signup'),

    #url(r'^$', views.index, name='index'),
     #url(r'^(?P<playlist-id>\d/+)$', views.index, name='select_playlist'),
     
]

'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
]'''