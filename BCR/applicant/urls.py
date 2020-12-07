from django.urls import path
from .views import applicantPageView, findAJobPageView

urlpatterns = [
    path("", applicantPageView, name="applicant"),
    path("findajob/", findAJobPageView, name="findajob"),
]