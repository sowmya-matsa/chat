from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    mobile = models.BigIntegerField(null=True, blank=True)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return str(self.mobile)


class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default=None)
    name = models.CharField(max_length=255, default="")
    about = models.CharField(max_length=255, default="")
    mobile_no = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.mobile_no)

    class Meta:
        verbose_name_plural = "profile"


class Settings(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    theme = models.CharField(max_length=255, default="")
    privacy=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "settings"


class IndividualChat(models.Model):
    name = models.CharField(max_length=255, default="")
    mobile_no = models.IntegerField()
    message = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.name) + "," + str(self.message)


class GroupChat(models.Model):
    group_name = models.CharField(max_length=255)
    group_image = models.ImageField(null=True, blank=True)
    members = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    group_chat = models.TextField()
    admin = models.BooleanField(default=True)
    description = models.TextField(default="")

    def __str__(self):
        return str(self.group_name) + "," + str(self.group_chat)


class Chat(models.Model):
    individual_chart = models.ForeignKey(IndividualChat, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    group_chat = models.ForeignKey(GroupChat, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Status(models.Model):
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255)
    contact = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    time = models.TimeField()
    status_privacy= models.CharField(max_length=255,default="")
    class Meta:
        verbose_name_plural = "Status"


class Call(models.Model):
    contact = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    mode_of_call = models.CharField(max_length=255,default="")
    type_of_call= models.CharField(max_length=255,default="")