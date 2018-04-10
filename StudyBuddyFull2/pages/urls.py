from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('pages/', views.DashboardView.as_view(), name='dashboard'),
]
