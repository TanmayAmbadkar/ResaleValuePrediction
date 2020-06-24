from django.urls import path
from SellerUI.views import *
from django.conf.urls import include

urlpatterns = [
    #path('', HomeView.as_view(), name = 'home'), #Home Page
    path('vehicle/<int:pk>', VehicleDetailView.as_view(), name = 'vehicle_detail'), #Whenever we want to view the entire details of a particular vehicle
    path('vehicles', VehicleListView.as_view(), name = 'vehicle_list'), #Whenever customer wants to view all published vehicles
    path('drafts/', DraftListView.as_view(), name = 'vehicle_draft_list'), # Whenever a seller wants to view his vehicles, posted and not posted
    path('vehicle/new/', CreateVehicleView.as_view(), name = 'vehicle_new'), # Add new vehicle
    path('vehicle/<int:pk>/edit', VehicleUpdateView.as_view(), name = 'vehicle_edit'), #Whenever a seller wants to edit details of a particular vehicle
    #path('user/new/', CreateUserView.as_view(), name = 'user_new'), #Creates a new user (unspecified)
    #path('profile/new/', CreateProfileView.as_view(), name = 'profile_new'), #Creates a profile for the user, helps him select whether User, Seller, Customer
    #path('profile<int:pk>', ProfileDetailView.as_view(), name = 'profile_detail'), #To view detials of the user
]
