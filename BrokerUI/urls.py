from django.conf.urls import url
from BrokerUI import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('',views.EstateListView.as_view(),name='home'),
    path('new/profile/',views.ProfileCreateView.as_view(),name='new_profile'), # new profile viz broker, user, seller
    path('new/user/',views.CreateUserView.as_view(),name='new_user'), # new user
    path('new/estate/',views.CreateEstateForm.as_view(),name='new_estate'), # new estate
    path('estate/<int:pk>',views.EstateDetailView.as_view(),name='estate_detail'),
    path('estate/<int:pk>/update',views.EstateUpdateView.as_view(),name='estate_update'),
    url('^broker/(?P<pk>[0-100]+)$',views.BrokerDetailView.as_view(),name='broker_detail'),
    path('broker/update/<int:pk>',views.BrokerUpdateView.as_view(),name='broker_update'),
    path('estate/<int:pk>/remove',views.EstateDeleteView.as_view(),name='estate_delete'),
    path('form/vehicle', views.EstatePricePrediction, name='predform'),
    path('search/',views.query,name='query'),
]
