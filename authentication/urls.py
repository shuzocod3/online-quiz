from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='quiz-list'), name='logout'),
    path('profile_edit/<int:pk>', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
]
