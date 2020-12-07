from django.urls import path
from .views import employerPageView

urlpatterns = [
    path("", employerPageView, name="employer")
]