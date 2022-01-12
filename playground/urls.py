from django.urls import path
from .views import PlayGroundView

urlpatterns = [
    path('', PlayGroundView.as_view(), name='playground'),
]