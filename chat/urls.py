from django.urls import path
from . import views
from .views import UserProfileAPIView, UserMessagesAPIView, ChatListAPIView, ChatDetailAPIView
    
urlpatterns = [
        path('api/user_profiles/<int:user_id>/', UserProfileAPIView.as_view(), name='user_profile_api'),
        path('api/user_messages/<int:user_id>/', UserMessagesAPIView.as_view(), name='user-messages-api'),
        path('api/chat_list/', ChatListAPIView.as_view(), name='chat-list-api'),
        path('api/chat/<str:chat_id>/', ChatDetailAPIView.as_view(), name='chat-detail-api')
]  