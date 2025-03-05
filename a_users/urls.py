from django.urls import path
from a_users.views import *

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('login/', ProfileLogin.as_view(), name="login"),
    path('register/', ProfileRegister.as_view(), name="register"),
    path('98765567890456789765456789/', ProfileDelete.as_view(), name="delete"),
    path('edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('usernamechange/', profile_usernamechange, name="profile-usernamechange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    # path('delete/', profile_delete_view, name="profile-delete"),
]
