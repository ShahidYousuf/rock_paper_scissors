from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from accounts.models import User


class PlayGroundView(View):
    template_name = "playground/home.html"

    def get(self, request, *args, **kwargs):
        playdroid = User.objects.get(username='PlayDroid')
        player = request.user
        context = {
            'playdroid': playdroid,
            'player': player
        }
        print(context)
        return render(request, self.template_name, context)
