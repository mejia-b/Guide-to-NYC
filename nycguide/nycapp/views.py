from django.shortcuts import render
from django.views import View
from boroughs import boroughs

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
