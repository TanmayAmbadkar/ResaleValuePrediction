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

    template_name = 'home.html'

class CreateVehicleView(LoginRequiredMixin, CreateView):

    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_draft_list')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

class VehicleUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'vehicle'
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
    redirect_field_name = 'VehicleUI/vehicle_draft_list.html'
    model = Vehicle
    template_name = 'vehicle_draft_list.html'

    def get_queryset(self):
        return Vehicle.objects.filter(seller=self.request.user)


class CreateSellerView(CreateView):

    template_name = 'seller_form.html'
    success_url = reverse_lazy('login')
    form_class = SellerProfileForm
    model = SellerProfile

class SellerDetailView(DetailView, LoginRequiredMixin):

    model = SellerProfile
    login_url = '/login/'
