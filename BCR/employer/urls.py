from django.urls import path
from .views import employerPageView, findApplicantsPageView, postJobPageView, applicantProfilePageView

urlpatterns = [
    path("", employerPageView, name="employer"),
    path("findapplicants/", findApplicantsPageView, name="findapplicants"),
    path('applicantprofile/', applicantProfilePageView, name="applicantprofile"),
    path('postjob/', postJobPageView, name="postjob"),
]