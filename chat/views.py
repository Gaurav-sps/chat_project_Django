from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, Message, Chat
from .serializers import UserProfileSerializer,MessageSerializer, ChatListSerializer
from rest_framework import generics
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProfileAPIView(APIView):
    def get(self, request, user_id):
        user_profiles = UserProfile.objects.filter(pk=user_id)
        serializer = UserProfileSerializer(user_profiles, many=True)
        print('helllo',serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
# def index(request):
#     	return render(request, 'index.html', {}) 

class UserMessagesAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(Q(sender=user_id) | Q(recipient=user_id)).order_by('timestamp')
    
# class ChatListAPIView(generics.ListAPIView):
#     serializer_class = ChatListSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user_name = self.request.user.username
#         user_profiles = UserProfile.objects.filter(name=user_name).first()
#         print("users",user_profiles)
#         return Chat.objects.filter(participants=user_profiles).order_by('-id')

# class ChatListAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         print('userrrrrrrr11111111')
#         user_profile = UserProfile.objects.get(name= 'Sarah Park')
#         print('userrrrrrrr',user_profile)

#         # Get chat list for the user
#         chat_list = Chat.objects.filter(participants=user_profile).order_by('-id')

#         # Prepare the response data
#         response_data = []
#         for chat in chat_list:
#             participants_data = [{
#                 'name': participant.name,
#                 'profile_pic': request.build_absolute_uri(participant.profile_pic.url) if participant.profile_pic else None,
#             } for participant in chat.participants.all()]

#             messages_data = [{
#                 'sender': message.sender.name,
#                 'content': message.content,
#                 'timestamp': message.timestamp,
#             } for message in chat.messages.all()]

#             response_data.append({
#                 'chat_id': chat.chat_id,
#                 'participants': participants_data,
#                 'messages': messages_data,
#             })

#         return Response(response_data)


class ChatListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(name= 'Sarah Park')

        # Get chat list for the user
        chat_list = Chat.objects.filter(participants=user_profile).order_by('-id')

        # Prepare the response data
        response_data = []
        for chat in chat_list:
            chat_data = {
                'chat_id': chat.chat_id,
                'messages': []
            }

            for message in chat.messages.all():
                message_data = {
                    'message': message.content,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'user_id': message.sender.user.id,
                    'username': message.sender.name,
                    'profile_pic': request.build_absolute_uri(message.sender.profile_pic.url) if message.sender.profile_pic else None,
                }

                chat_data['messages'].append(message_data)

            response_data.append(chat_data)

        return Response(response_data)