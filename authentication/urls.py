from django.urls import path
from .views import UserCreateView, VerifyEmail

urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('activate/<uid>/<str:token>/', VerifyEmail.as_view())
]
