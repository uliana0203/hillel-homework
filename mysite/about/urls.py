from django.urls import path, re_path
from .views import whoami, source_code, random

app_name = 'about'

urlpatterns = [
    path('whoami/', whoami),
    path('source_code/', source_code),
    path('random/', random)
]