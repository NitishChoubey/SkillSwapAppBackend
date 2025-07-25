from django.urls import path
from .views import RegisterView, LoginView , ProfileUpdateView , ProfilePictureUploadView

urlpatterns = [
    path('register/', RegisterView.as_view() ),
    path('login/', LoginView.as_view() ) ,
    path('profile/update/' , ProfileUpdateView.as_view() , name = 'profile-update'),
    path('profile/picture/upload/' , ProfilePictureUploadView.as_view() ,name= 'profile-picture-upload' )
]
