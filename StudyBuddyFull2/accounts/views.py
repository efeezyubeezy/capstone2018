import string

import random
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, RegistrationForm

from django.http import HttpResponseRedirect, request

from django.contrib.auth.decorators import login_required

from .models import CustomUser, Profile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('accounts:signup2')
	template_name = 'signup.html'


class Registration(generic.FormView):
	form_class = RegistrationForm
	success_url = reverse_lazy('login')
	template_name = 'signup2.html'


@login_required
@transaction.atomic
def create_profile(request):
	if request.method == 'POST':
		user_form = CustomUser(request.POST, instance=request.user)
		profile_form = RegistrationForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'profile successfully updated!')
			return redirect('settings:profile')
		else:
			messages.error(request, 'please correct error below.')
	else:
		user_form = CustomUser(instance=request.user)
		profile_form = RegistrationForm(instance=request.user.profile)
	return render(request, 'accounts/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})


class DashboardView(TemplateView):
	template_name = 'dashboard.html'


class ProfileView(TemplateView):
	template_name = 'profile.html'


class ProfileUpdate(generic.UpdateView):

	def get_pk(self):
		return self.kwargs['pk']
	model = Profile
	success_url = reverse_lazy('accounts:profile_update_success')
	template_name = 'profile_update.html'
	form_class = RegistrationForm

	def update_profile(self, request, user_id):
		user = CustomUser.objects.get(pk=user_id)

		# user.profile.first_name = ''
		# user.profile.mid_name = ''
		# user.profile.last_name = ''
		# user.profile.dob = ''
		# user.profile.usr_stat = ''
		# user.profile.phone_number = ''
		# user.profile.address = ''
		# user.profile.country = ''
		# user.profile.state = ''
		# user.profile.city = ''
		# user.profile.zip_code = ''
		# user.profile.sex = ''
		# user.profile.race_ethnicity = ''
		# user.profile.employment = ''
		# user.profile.education = ''
		# user.profile.degree = ''
		# user.profile.university = ''
		# user.profile.live_online = ''
		# user.profile.classroom = ''
		# user.profile.profile_image = ''

		user.profile.save()


@login_required
@transaction.atomic
def update_profile(request):
	if request.method == 'POST':
		profile = Profile.objects.get(user=request.user)
		profile_form = RegistrationForm(request.POST, instance=request.user.profile)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, 'profile successfully updated!')
			return redirect('settings:profile_update_success')
		else:
			messages.error(request, 'please correct error below.')
	else:
		profile_form = RegistrationForm(instance=request.user.profile)
	return render(request, 'accounts/profile_update_success.html', {
		'profile_form': profile_form
	})


class ProfileSuccess(TemplateView):

	def get_pk(self):
		return self.kwargs['pk']
	template_name = 'profile_update_success.html'
	success_url = reverse_lazy('accounts:profile')
