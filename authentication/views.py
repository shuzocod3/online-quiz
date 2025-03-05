from django.contrib.auth.mixins import LoginRequiredMixin
from authentication import models
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from .models import CustomUser

# Create your views here.
class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'authentication/edit_profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class ProfileDetailView(DetailView):
    model = models.CustomUser
    context_object_name = "profile"
    template_name = "authentication/profile.html"