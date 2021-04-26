from django.urls import path
from .views import editJobResponsePageView, employerPageView, findApplicantsPageView, findApplicantsResponsePageView, postJobPageView, applicantProfilePageView, reviewApplicantsPageView, editEmployerProfilePageView, applicantListingsPageView, empMyAccountPageView, jobPostedPageView, editJobPageView, editJobResponsePageView, editJobSuccessPageView

urlpatterns = [
    path("", employerPageView, name="employer"),
    path("findapplicants/", findApplicantsPageView, name="findapplicants"),
    path("findapplicants/response", findApplicantsResponsePageView, name="findapplicantsresponse"),
    path("applicantlistings/", applicantListingsPageView, name="applicantlistings"),
    path("reviewapplicants/", reviewApplicantsPageView, name="reviewapplicants"),
    path('applicantprofile/', applicantProfilePageView, name="applicantprofile"),
    path('postjob/', postJobPageView, name="postjob"),
    path('editjob/', editJobPageView, name="editjob"),
    path('editjob/form', editJobResponsePageView, name="editjobresponse"),
    path('editjob/success', editJobSuccessPageView, name='editjobsuccess'),
    path('editemployerprofile/', editEmployerProfilePageView, name = "editemployerprofile"),
    path('myaccount/', empMyAccountPageView, name="empmyaccount"),
    path('jobposted/', jobPostedPageView, name="jobposted")
]



