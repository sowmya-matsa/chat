from django.contrib import admin
from .models import CustomUser, Settings, IndividualChat, GroupChat, Call, Status


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_pic', 'name', 'about', 'mobile_no']


class IndividualChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_no']


class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group_image', 'add_user']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'caption', 'contact', 'time']


class CallAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'type_of_call']


admin.site.register(CustomUser)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(IndividualChat, IndividualChatAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register(Status, StatusAdmin)