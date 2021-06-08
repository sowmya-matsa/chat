from django.contrib import admin
from .models import CustomUser, Settings, IndividualChat, GroupChat, Call, Status, Profile, Chat


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'theme', 'privacy']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_pic', 'name', 'about', 'mobile_no']


class IndividualChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile_no','message']


class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'group_image', 'members', 'admin', 'description','group_chat']


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'individual_chart', 'group_chat']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'caption', 'contact', 'time', 'status_privacy']


class CallAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'type_of_call', 'mode_of_call']


admin.site.register(CustomUser)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(IndividualChat, IndividualChatAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register(Status, StatusAdmin)
