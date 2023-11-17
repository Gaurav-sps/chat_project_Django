from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Chat(models.Model):
    participants = models.ManyToManyField(UserProfile, related_name='chats')
    chat_id = models.CharField(max_length=255, unique=True,default='default_chat_id')

    def __str__(self):
        return f"Chat {self.chat_id}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE, default=1)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} in Chat {self.chat_id} - {self.timestamp}"
