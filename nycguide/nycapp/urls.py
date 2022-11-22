from django.urls import path
from nycapp.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
]
