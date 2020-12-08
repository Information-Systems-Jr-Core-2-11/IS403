from django.urls import path
from .views import employerPageView, findApplicantsPageView, postJobPageView, applicantProfilePageView, reviewApplicantsPageView, editEmployerProfilePageView, applicantListingsPageView

urlpatterns = [
    path("", employerPageView, name="employer"),
    path("findapplicants/", findApplicantsPageView, name="findapplicants"),
    path("applicantlistings/", applicantListingsPageView, name="applicantlistings"),
    path("reviewapplicants/", reviewApplicantsPageView, name="reviewapplicants"),
    path('applicantprofile/', applicantProfilePageView, name="applicantprofile"),
    path('postjob/', postJobPageView, name="postjob"),
    path('editemployerprofile/', editEmployerProfilePageView, name = "editemployerprofile")
]



