from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    mobile = models.BigIntegerField(null=True, blank=True)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return str(self.mobile)


class Settings(models.Model):
    profile_pic = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    mobile_no = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, default=None)


    def __str__(self):
        return str(self.mobile_no)

    class Meta:
        verbose_name_plural = "settings"


class IndividualChat(models.Model):
    mobile_no = models.IntegerField()


class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    group_image = models.ImageField(null=True, blank=True)
    add_user = models.ForeignKey(Settings, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    chat = models.TextField()


class Status(models.Model):
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255)
    contact = models.ForeignKey(Settings, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    time= models.TimeField()

    class Meta:
        verbose_name_plural = "Status"
class Call(models.Model):
    contact = models.ForeignKey(Settings, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    type_of_call = models.CharField(max_length=255)
