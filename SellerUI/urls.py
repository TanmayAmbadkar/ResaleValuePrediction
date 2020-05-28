from django.urls import path
from SellerUI.views import *
from django.conf.urls import include

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('vehicle/<int:pk>', VehicleDetailView.as_view(), name = 'vehicle_detail'),
    path('vehicles', VehicleListView.as_view(), name = 'vehicle_list'),
    path('drafts/', DraftListView.as_view(), name = 'vehicle_draft_list'),
    path('vehicle/new/', CreateVehicleView.as_view(), name = 'vehicle_new'),
    path('vehicle/<int:pk>/edit', VehicleUpdateView.as_view(), name = 'vehicle_edit'),
    path('user/new/', CreateUserView.as_view(), name = 'user_new'),
    path('seller/new/', CreateProfileView.as_view(), name = 'seller_new'),
    path('seller/<int:pk>', ProfileDetailView.as_view(), name = 'seller_detail'),
]
