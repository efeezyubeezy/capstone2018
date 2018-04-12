from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('registration/', views.Registration.as_view(), name='signup2'),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('profile/', views.ProfileView.as_view(), name='profile'),
	path('profile_update/<int:pk>/', views.ProfileUpdate.as_view(), name='profile_update'),
	path('profile_update_success/<int:pk>/', views.ProfileSuccess.as_view(), name='profile_update_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
