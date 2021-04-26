from django.contrib import admin
from .models import Organization, Job, Applicant, Job_Offer, Application_Status, Job_Application, Work_Experience, School_Experience, Skill, Applicant_Skill, Job_Skill

# Register your models here.
admin.site.register(Organization)
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Job_Offer)
admin.site.register(Application_Status)
admin.site.register(Job_Application)
admin.site.register(Work_Experience)
admin.site.register(School_Experience)
admin.site.register(Skill)
admin.site.register(Applicant_Skill)
admin.site.register(Job_Skill)
