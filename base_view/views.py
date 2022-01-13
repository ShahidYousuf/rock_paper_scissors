import datetime
import json
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import login
from accounts.forms import RegisterForm
from accounts.models import User


class HomeView(View):
    template_name = "base_view/home.html"
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        context = {
            'register_form': self.form_class(),
            'message': 'Welcome to Home of Rock, Paper and Scissors',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            user = self._create_user(**register_form.cleaned_data)
            if user is not None:
                login(request, user)
                # redirect to playground
            context = {
                'user_registered': True,
                'next': '/'
            }
            return JsonResponse(context)
        else:
            error_dict = json.loads(register_form.errors.as_json())
            context = {
                'register_form_errors': error_dict,
                'user_registered': False
            }

            return JsonResponse(context)

    def _create_user(self, *args, **kwargs):
        full_name = kwargs.get('name', '')
        parts = full_name.split()
        first_name, last_name = parts[0], ' '.join(parts[1:])
        username = full_name.replace(" ", "_") + str(int(datetime.datetime.now().timestamp()))
        email = username + "@localhost.com"
        password = full_name + "123"
        user = User.objects.filter(first_name=first_name, last_name=last_name)
        if user.exists():
            return user.first()
        user = User(first_name=first_name, last_name=last_name)
        user.email = email
        user.set_password(password)
        user.is_active = True
        user.username = username
        user.save()
        return user





