from django.shortcuts import render
from django.views import View

from accounts.forms import RegisterForm

class HomeView(View):
    template_name = "base_view/home.html"
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        context = {
            'register_form': self.form_class(),
            'message': 'Welcome to Home of Rock, Paper and Scissors',
        }
        return render(request, self.template_name, context)
