from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "base_view/home.html"

    def get(self, request, *args, **kwargs):
        context = {
            'message': 'Welcome to Home of Rock, Paper and Scissors',
        }
        return render(request, self.template_name, context)
