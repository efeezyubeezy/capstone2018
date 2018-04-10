from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm, RegistrationForm

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .models import CustomUser
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('accounts:signup2')
	template_name = 'signup.html'


class Registration(generic.FormView):
	form_class = RegistrationForm
	success_url = reverse_lazy('dashboard')
	template_name = 'signup2.html'

	def get_user_name(self, request):
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				return HttpResponseRedirect('accounts:profile')
		else:
			form = RegistrationForm()

		return render(request, 'signup2.html', {'form': form})


class DashboardView(TemplateView):
	template_name = 'dashboard.html'


class ProfileView(TemplateView):
	template_name = 'profile.html'

	def update_profile(self, request, user_id):
		user = CustomUser.objects.get(pk=user_id)

		user.profile.first_name = '...'
		user.profile.mid_name = '...'
		user.profile.last_name = '...'
		user.profile.dob = '...'
		user.profile.usr_stat = '...'
		user.profile.phone_number = '...'
		user.profile.address = '...'
		user.profile.country = '...'
		user.profile.state = '...'
		user.profile.city = '...'
		user.profile.zip_code = '...'
		user.profile.sex = '...'
		user.profile.race_ethnicity = '...'
		user.profile.employment = '...'
		user.profile.education = '...'
		user.profile.degree = '...'
		user.profile.university = '...'
		user.profile.live_online = '...'
		user.profile.classroom = '...'
		user.profile.profile_image = '...'
		user.save()


@login_required
@transaction.atomic
def update_profile(request):
	if request.method == 'POST':
		user_form = CustomUser(request.POST, instance=request.user)
		profile_form = RegistrationForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, _('profile successfully updated!'))
			return redirect('settings:profile')
		else:
			messages.error(request, _('please correct error below.'))
	else:
		user_form = CustomUser(instance=request.user)
		profile_form = RegistrationForm(instance=request.user.profile)
	return render(request, 'accounts/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})


#
# 	@login_required()
# 	def edit_user(self, request, pk):
# 		user = CustomUser.objects.get(pk=pk)
# 		user_form = RegistrationForm(instance=user)
#
# 		ProfileInlineFormset = inlineformset_factory(CustomUser, CustomUser, fields=('email',
# 		                'usr_stat', 'first_name', 'mid_name', 'last_name',
# 		                'dob', 'phone_number', 'address', 'country',
# 		                'state', 'city', 'zip_code', 'sex',
# 		                'race_ethnicity', 'employment', 'education',
# 		                'degree', 'university', 'live_online',
# 		                'classroom', 'profile_image',))
# 		formset = ProfileInlineFormset(instance=user)
#
# 		if request.user.is_authenticated() and request.user.id == user.id:
# 			if request.method == 'POST':
# 				user_form = RegistrationForm(request.POST, request.FILES, instance=user)
# 				formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
#
# 				if user_form.is_valid():
# 					created_user = user_form.save(commit=False)
# 					formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
#
# 					if formset.is_valid():
# 						created_user.save()
# 						formset.save()
# 						return HttpResponseRedirect('/accounts/profile/')
# 			return render(request, 'account/account_update.html', {
# 				'noodle': pk,
# 				'noodle_form': user_form,
# 				'formset': formset,
# 			})
# 		else:
# 			raise PermissionDenied
