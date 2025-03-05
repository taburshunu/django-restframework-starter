from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import *
from .forms import *

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username=None):
        if username:
            profile = get_object_or_404(User, username=username).profile
        else:
            if not request.user.is_authenticated:
                return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
            profile = request.user.profile

        serializer = ProfileSerializer(profile) 
        return Response(serializer.data)
    


@login_required
@api_view(['GET', 'POST'])
def profile_edit_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('profile')  # Redirect after saving

        return Response(serializer.errors, status=400)  # Return errors if invalid

    serializer = ProfileSerializer(profile)
    
    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False

    return Response({"data": serializer.data, "onboarding": onboarding})

@login_required
@api_view(['GET'])
def profile_settings_view(request):
    if not request.user.email:
        pass
    else:
        return Response({"message": "Profile settings view", "user": request.user.username, "email": request.user.email})

@login_required
@api_view(['GET', 'POST'])
def profile_emailchange(request):
    if request.headers.get("HX-Request"):  # HTMX detection
        serializer = EmailSerializer(instance=request.user)

        return Response({"serializer": serializer.data})  # Return serialized data

    return Response({"error": "Invalid request"}, status=400)


@api_view(['GET', 'POST'])
@login_required
def profile_usernamechange(request):
    if request.headers.get("HX-Request"):
        serializer = UsernameSerializer(instance=request.user)
        return Response({"serializer": serializer.data})  # Return serialized data

    return Response({"error": "Invalid request"}, status=400)


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    logout(request)
    user.delete()
    messages.success(request, 'Account deleted, what a pity')
    return redirect('home')
