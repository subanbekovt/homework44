from django.urls import path

from webapp_cows_and_bulls.views import main_view, log_view

urlpatterns = [
    path('', main_view),
    path('log/', log_view)
]