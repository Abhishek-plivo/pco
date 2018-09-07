from django.urls import path, re_path
from .views import CallAgent


urlpatterns = [
    path('call_agent/', CallAgent.as_view(), name="call_agent"),
]
