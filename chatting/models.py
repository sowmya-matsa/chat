from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    mobile = models.BigIntegerField(null=True, blank=True)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return str(self.mobile)


class Contacts(models.Model):
    name = models.CharField(max_length=255, default="")
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "contacts"


class Settings(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default=None)
    name = models.CharField(max_length=255, default="")
    about = models.CharField(max_length=255, default="")
    mobile_no = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    theme = models.CharField(max_length=255, default="")
    last_seen = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "settings"


class IndividualChat(models.Model):
    contact_name = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    message = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.contact_name) + "," + str(self.message)


class GroupChat(models.Model):
    group_name = models.CharField(max_length=255)
    group_image = models.ImageField(null=True, blank=True)
    members = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    group_chat = models.TextField()
    admin = models.BooleanField(default=True)
    description = models.TextField(default="")
    creator_name = models.CharField(max_length=255, default="")
    created_date = models.DateField()

    def __str__(self):
        return str(self.group_name) + "," + str(self.group_chat)


class Chat(models.Model):
    individual_chat = models.ForeignKey(IndividualChat, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    group_chat = models.ForeignKey(GroupChat, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Status(models.Model):
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255)
    time = models.TimeField()
    status_privacy = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Status"


class Call(models.Model):
    contact = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    mode_of_call = models.CharField(max_length=255, default="")
    type_of_call = models.CharField(max_length=255, default="")
