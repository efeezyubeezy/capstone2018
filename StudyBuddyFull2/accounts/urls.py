from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('registration/', views.Registration.as_view(), name='signup2'),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('profile/', views.ProfileView.as_view(), name='profile'),
]
