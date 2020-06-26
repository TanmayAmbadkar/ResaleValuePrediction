from django.urls import path
from UserUI.views import *
from django.conf.urls import include

urlpatterns = [
    path('user/vehicles', VehiclesBoughtView.as_view(), name = 'vehicles'), #Home Page
]
