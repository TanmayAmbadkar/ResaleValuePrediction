from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from SellerUI.models import *
from BrokerUI.models import *
from UserUI.models import *

# Create your views here.

class VehiclesBoughtView(TemplateView):

    template_name = 'UserUI/vehicles_bought.html'

    def get_context_data(self, **kwargs):

        context = super(VehiclesBoughtView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        vehicles = VehiclesBought.objects.filter(buyer = profile)
        context['vehicles'] = vehicles
        return context
