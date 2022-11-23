from django.urls import path
from nycapp.views import HomeView, BoroughView, ActivityView, VenueView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<str:borough>',BoroughView.as_view(), name='borough'),
    path('<str:borough>/<str:activity>', ActivityView.as_view(), name='activity'),
    path('<str:borough>/<str:activity>/<str:venue>', VenueView.as_view(), name='venue'),
]
