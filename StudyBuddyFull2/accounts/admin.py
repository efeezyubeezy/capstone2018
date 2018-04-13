from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


class CustomUserInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'


class CustomUserAdmin(UserAdmin):
	inlines = (CustomUserInline, )
	model = CustomUser
	can_delete = False
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ('username', 'first_name', 'last_name',
	                'email', 'id', 'password',
	                'last_login', 'date_joined',
	                )

	list_select_related = ('profile',)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
