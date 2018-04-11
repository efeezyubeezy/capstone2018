from datetime import date

import os

from django.conf import settings
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.urls import reverse

from django.contrib.auth.models import AbstractUser, UserManager, User

from phonenumber_field.modelfields import PhoneNumberField

from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUserManager(UserManager):
	pass


class CustomUser(AbstractUser):
	objects = CustomUserManager()

	def __str__(self):
		return self.email

	def is_valid(self):
		pass


class Profile(models.Model):
	objects = CustomUserManager()

	username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

	first_name = models.CharField(blank=True, max_length=50, default='')
	mid_name = models.CharField(blank=True, max_length=50, default='')
	last_name = models.CharField(blank=True, max_length=50, default='')
	dob = models.DateField(blank=True, default=date.today)
	usr_stat = models.CharField(blank=True, max_length=20, default='')
	phone_number = PhoneNumberField(blank=True, max_length=30, default='')
	address = models.CharField(blank=True, max_length=50, default='')
	country = models.CharField(blank=True, max_length=50, default='')
	state = models.CharField(blank=True, max_length=2, default='')
	city = models.CharField(blank=True, max_length=50, default='')
	zip_code = models.CharField(blank=True, max_length=25, default='')
	sex = models.CharField(blank=True, max_length=5, default='')
	race_ethnicity = models.CharField(blank=True, max_length=100, default='')
	employment = models.CharField(blank=True, max_length=5, default='')
	education = models.CharField(blank=True, max_length=4, default='')
	degree = models.CharField(blank=True, max_length=50, default='')
	university = models.CharField(blank=True, max_length=50, default='')
	live_online = models.CharField(blank=True, max_length=5, default='')
	classroom = models.CharField(blank=True, max_length=10, default='')
	# availability = models.  same issue as in forms/ how to display as calendar???

	def get_image_path(self, filename):
		return os.path.join('images', str(self.pk), filename)

	profile_image = models.FileField(verbose_name='profile image',
	                                 upload_to=get_image_path, blank=True,
	                                 null=True)

	def __str__(self):
		return self.username

	def is_valid(self):
		pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	if not created:
		return
	Profile.objects.create(user=instance)
	post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='save_new_user_profile')
def save_user_profile(sender, instance, created, **kwargs):
	user = instance
	if created:
		profile = Profile(user=user)
		profile.save()
	instance.profile.save()


users = CustomUser.objects.all().select_related('profile')
