from django.contrib import admin
from .models import CustomUser, Settings, IndividualChat, GroupChat, Call, Status, Chat, Contacts


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_pic', 'name', 'about', 'mobile_no', 'theme', 'last_seen', 'mobile_no']


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number']


class IndividualChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_name', 'message', 'state']


class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'group_image', 'members', 'admin', 'description', 'group_chat', 'creator_name',
                    'created_date']


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'individual_chat', 'group_chat']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'caption', 'time', 'status_privacy']


class CallAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'type_of_call', 'mode_of_call']


admin.site.register(CustomUser)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(IndividualChat, IndividualChatAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register(Status, StatusAdmin)
