from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm, RegistrationForm
from .models import CustomUser, Profile


class CustomUserInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	# fk_name = settings.AUTH_USER_MODEL
	fields = ['accounts.CustomUser', ]


class CustomUserAdmin(UserAdmin):
	inlines = (CustomUserInline, )
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ('username', 'email',

	                )

	list_select_related = ('profile',)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# class ProfileInline(admin.StackedInline):
# 	model = Profile
# 	can_delete = False
# 	verbose_name_plural = 'Profile'
# 	fields = ['accounts.CustomUser', ]


# class ProfileAdmin(UserAdmin):
# 	inlines = (ProfileInline, )
# 	model = Profile
# 	add_form = RegistrationForm
# 	list_display = ('usr_stat', 'first_name', 'mid_name', 'last_name',
# 	                'dob', 'phone_number', 'address', 'country',
# 	                'state', 'city', 'zip_code', 'sex',
# 	                'race_ethnicity', 'employment', 'education',
# 	                'degree', 'university', 'live_online',
# 	                'classroom', 'profile_image', )
# 	list_select_related = ('profile',)
#
# 	def get_inline_instances(self, request, obj=None):
# 		if not obj:
# 			return list()
# 		return super(ProfileAdmin, self).get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
