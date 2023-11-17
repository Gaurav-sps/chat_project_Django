from django.contrib import admin
from .models import UserProfile, Message, Chat
    
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Chat)