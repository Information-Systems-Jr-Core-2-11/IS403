from django.urls import path
from .views import applicantPageView, findAJobPageView, jobListingsPageView, skillRecommenderPageView, jobDetailsPageView, companyProfilePageView, skillRecommenderResponsePageView, offersPageView

urlpatterns = [
    path("", applicantPageView, name="applicant"),
    path("findajob/", findAJobPageView, name="findajob"),
    path("joblistings/", jobListingsPageView, name="joblistings"),
    path("joblistings/jobdetails/", jobDetailsPageView, name="jobdetails"),
    path("companyprofile/", companyProfilePageView, name="companyprofile"),
    path("skillrecommender/", skillRecommenderPageView, name="skillrecommender"),
    path("skillrecommender/response/", skillRecommenderResponsePageView, name="skillrecommenderresponse"),
    path("offers", offersPageView, name="offers")
]