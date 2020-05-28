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

    #TemplateView is the most basic view. By default, it just loads a page set as its template_name
    #We can add a context_dict using get_context_data to pass values to the page
    template_name = 'SellerUI/home.html'

class CreateVehicleView(LoginRequiredMixin, CreateView):

    #The createview helps create a new object for the model specified. LoginRequiredMixin is same is decorators
    #the form class loads the form from which data is collected
    #After form validation, we load the home page using reverse_lazy
    # in the form validation, I am finding the Profile of the user who filled to form.
    #This is required because I have to attach the vehicle to the Seller, and so I am attaching it to the form.instance which is vehicle_edit
    # Vehicle.seller = profile

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('home')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

    def form_valid(self, form):
        profile = Profile.objects.get_or_create(user = self.request.user)[0]
        print(profile)
        form.instance.seller = profile
        form.instance.save()
        return super().form_valid(form)

class VehicleUpdateView(LoginRequiredMixin, UpdateView):

    #The update view just changes the parameters of an already created object.
    # We specify <int:pk> in the url to get the specific object to update

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('vehicle_draft_list')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

class VehicleDetailView(DetailView):

    #Simply sends a single object pk = <int:pk> to the page.
    #the context dict is a single object, which could be changed using get_context_data

    model = Vehicle

class VehicleListView(ListView):
    #Simply sends all objects of the model to page.
    #the context dict is aall objects, which could be changed using get_context_data

    model = Vehicle


class DraftListView(LoginRequiredMixin, ListView):

    #to get the draft vehicles only for the seller that has requested it
    #I have selected the profile from the request.user, then selected all vehicle
    # objects made by that user and send it to the context_dict

    login_url = '/login/'
    model = Vehicle
    template_name = 'SellerUI/vehicle_draft_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        profile = Profile.objects.filter(user = self.request.user)[0]
        return Vehicle.objects.filter(seller = profile)

class CreateUserView(CreateView):

    #Creates new user, no profile.
    #To set password, i have to use the set_password method

    template_name = 'SellerUI/user_form.html'
    success_url = reverse_lazy('home')
    form_class = UserForm
    model = User
    def form_valid(self, form):

        form.instance.set_password(form.instance.password)
        return super().form_valid(form)

class CreateProfileView(CreateView):

    #This is second step in registration, which sets the profile, whether customer,
    # buyer or seller. Form has options available.
    # I have to set the foreign key so I am getting the user who is registering and
    # attaching it to the foreign key

    template_name = 'SellerUI/profile_form.html'
    success_url = reverse_lazy('home')
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):

        form.instance.user = User.objects.filter(username = self.request.user.username)[0]
        return super().form_valid(form)

class ProfileDetailView(DetailView, LoginRequiredMixin):

    model = Profile
    login_url = '/login/'
