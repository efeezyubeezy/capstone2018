from django.forms import ChoiceField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
import datetime

from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import SelectDateWidget, ClearableFileInput

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields


class RegistrationForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		user = CustomUser
		fields = ['first_name', 'mid_name', 'last_name', 'dob',
				  'usr_stat', 'phone_number', 'address', 'country',
				  'state', 'city', 'zip_code', 'sex', 'race_ethnicity',
				  'employment', 'education', 'degree', 'university',
				  'live_online', 'classroom', 'profile_image', ]

	USRTYPE = [('S', 'student'),
	           ('T', 'tutor')]

	usr_stat = forms.ChoiceField(
		label='student/ tutor', choices=USRTYPE,
		widget=forms.Select(attrs={'class': 'regDropDown'}))

	first_name = forms.CharField(label='first name', max_length=50, required=True)

	mid_name = forms.CharField(label='middle name', max_length=50, required=False)

	last_name = forms.CharField(label='last name', max_length=50, required=True)

	dob = forms.DateField(widget=SelectDateWidget(
		years=range(1920, datetime.date.today().year+10)),
		label='date of birth', required=True)

	phone_number = PhoneNumberField(
		label='phone number',
		required=True,
		widget=PhoneNumberInternationalFallbackWidget())

	address = forms.CharField(label='street address', max_length=50, required=True)

	country = forms.CharField(label='country', max_length=50, required=True)

	state = forms.CharField(label='state/ province', max_length=2, required=True)

	city = forms.CharField(label='city', max_length=50, required=True)

	zip_code = forms.CharField(label='zip code', max_length=25, required=True)

	SEX = [('m', 'male'), ('f', 'female'), ('u', 'undisclosed')]

	sex = ChoiceField(label='sex', choices=SEX,
	                  widget=forms.Select(attrs={'class': 'regDropDown'}))

	RACE = [('x', '----'),
	        ('b', 'black/ african american'),
	        ('l', 'latinx'),
	        ('a', 'asian'),
	        ('n', 'american indian/ alaska native'),
	        ('w', 'white/ european american')]

	race_ethnicity = ChoiceField(label='race/ ethnicity', choices=RACE,
	                             widget=forms.Select(attrs={'class': 'regDropDown'}))

	EMPLOYED = [('y', 'yes'),
	            ('n', 'no')]

	employment = ChoiceField(
		label='are you currently employed?',
		choices=EMPLOYED,
		widget=forms.Select(
			attrs={'class': 'regDropDown'}))

	EDUCATION = [('EL', 'elementary school'),
	             ('MS', 'middle school'),
	             ('HS', 'high school',),
	             ('UG1', 'college (AA)'),
	             ('UG2', 'college (BA)'),
	             ('MA', 'graduate school (masters)'),
	             ('PHD', 'graduate school (complete)')]

	education = ChoiceField(label='current/ highest education level?',
	                        choices=EDUCATION,
	                        widget=forms.Select(attrs={'class': 'regDropDown'}))

	degree = forms.CharField(label='area of focus/ degree?', max_length=50,
	                         required=True)

	university = forms.CharField(label='university/ college you obtained degree from?',
	                             max_length=75, required=True)

	LIVE_ONLINE = [('l', 'live tutor'),
	               ('ol', 'online tutor'),
	               ('lol', 'both')]

	live_online = ChoiceField(label='live tutor, an online tutor, or both?',
	                          choices=LIVE_ONLINE,
	                          widget=forms.Select(attrs={'class': 'regDropDown'}))

	CLASSROOM = [('pub', 'public'),
	            ('priv', 'private'),
	            ('flex', 'flexible')]

	classroom = ChoiceField(label='preferred learning environment:',
	                        choices=CLASSROOM,
	                        widget=forms.Select(attrs={'class': 'regDropDown'}))

	# def clean_profile_image(self):
	# 	profile_image = self.cleaned_data['profile_image']
	#
	# 	try:
	# 		w, h = get_image_dimensions(profile_image)
	#
	# 		max_width = max_height = 100
	# 		if w > max_width or h > max_height:
	# 			raise forms.ValidationError(
	# 				u'please use an image that is '
	# 				'%s x %s pixels or smaller.'
	# 				% (max_width, max_height))
	#
	# 		main, sub = profile_image.content_type.split('/')
	# 		if not (main == 'image' and sub in ['jpeg', 'pjpeg',
	# 		                                    'gif', 'png']):
	# 			raise forms.ValidationError(
	# 				u'please use a jpeg, GIF, or PNG image.')
	#
	# 		if len(profile_image) > (20 * 1024):
	# 			raise forms.ValidationError(
	# 				u'avatar file size may not exceed 20k.')
	#
	# 	except AttributeError:
	# 		pass
	#
	# 	return profile_image

	profile_image = forms.ImageField(label='profile image', widget=ClearableFileInput, required=False)

	# availability = want to make a calendar type of deal so people can pick available days & then times for those days???

	def save(self, user=None):
		user_profile = super(RegistrationForm, self).save(commit=False)
		if user:
			user_profile.user = user
		user_profile.save()
		return user_profile

