from django.urls import path
from nycapp.views import HomeView, BoroughView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<str:borough>',BoroughView.as_view(), name='borough'),
]
