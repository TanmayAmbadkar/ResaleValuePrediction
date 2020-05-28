from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from SellerUI.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from SellerUI.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
# Create your views here.

# Create your views here.

class HomeView(TemplateView):

    template_name = 'SellerUI/home.html'

class CreateVehicleView(LoginRequiredMixin, CreateView):

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('vehicle_draft_list')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

    def form_valid(self, form):

        form.instance.seller = Profile.objects.filter(username = self.request.user.usernmae)
        return super().form_valid(form)

class VehicleUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('vehicle_draft_list')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

class VehicleDetailView(DetailView):

    model = Vehicle

class VehicleListView(ListView):

    model = Vehicle


class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'SellerUI/vehicle_draft_list.html'
    model = Vehicle
    template_name = 'vehicle_draft_list.html'

    def get_queryset(self):
        return Vehicle.objects.filter(seller=self.request.user)


class CreateUserView(CreateView):

    template_name = 'SellerUI/user_form.html'
    success_url = reverse_lazy('home')
    form_class = UserForm
    model = User
    def form_valid(self, form):

        form.instance.set_password(form.instance.password)
        return super().form_valid(form)

class CreateProfileView(CreateView):

    template_name = 'SellerUI/seller_form.html'
    success_url = reverse_lazy('login')
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):

        form.instance.user = User.objects.filter(username = self.request.user.username)[0]
        return super().form_valid(form)

class ProfileDetailView(DetailView, LoginRequiredMixin):

    model = Profile
    login_url = '/login/'
