from django.urls import path
from .views import homePageView, loginPageView, ourMissionPageView, signupEmployerPageView, signupPageView, signupApplicantPageView

urlpatterns = [
    path("", homePageView, name="homepage"),
    path("ourmission/", ourMissionPageView, name="ourmission"),
    path("login/", loginPageView, name="login"),
    path("signup/", signupPageView, name="signupmain"),
    path('signup/employer', signupEmployerPageView, name='signupemployer'),
    path('signup/applicant', signupApplicantPageView, name='signupapplicant'),
    path("ourmission/", ourMissionPageView, name="ourmission"),

]