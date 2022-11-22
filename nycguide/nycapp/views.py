from django.shortcuts import render
from django.views import View
from nycapp.boroughs import boroughs

# Create class views

class HomeView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'home.html',
            context = {
                'boroughs': boroughs.keys(),
            }
        )

class BoroughView(View):
   def get(self,request,borough):
    return render(
        request = request,
        template_name = 'borough.html',
        context = {'borough': borough, 'activities': boroughs[borough].keys()},
    )

class ActivityView(View):
    pass