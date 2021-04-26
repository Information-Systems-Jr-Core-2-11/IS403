from django.shortcuts import render
from .models import Skill, Applicant_Skill, Job, Job_Skill, Organization
from django.db import connection

# Create your views here.
def employerPageView(request):
    return render(request, 'employer/index.html')

def findApplicantsPageView(request):
    jobs = Job.objects.filter(organization_id_id = 201)
    context = {'Jobs' : jobs}
    return render(request, 'employer/findapplicants.html', context)

def findApplicantsResponsePageView(request):
    if request.method == 'POST':
    
        job_id = request.POST.get('choices-multiple-remove-button')
        query = MatchingAppsSQL(job_id) 




        # because I need to pull data using a query that joins tables and runs an aggregate (to find number of matching skills per job adaptively),
        # I cannot map to the models and use a cursor object to link directly to the database. https://docs.djangoproject.com/en/dev/topics/db/sql/ <-- executing custom SQL directly
        cursor = connection.cursor()
        cursor.execute(query) # executes SQL query generated from MatchingJobsSQL function
        matching_users = cursor.fetchall()

        context = {
            'matchingUsers' : matching_users,
        }
        return render(request, 'employer/findapplicantsresponse.html', context)

    return render(request, 'employer/findapplicantsresponse.html')

def applicantListingsPageView(request):
    if request.method == 'POST':
        selected_skills = request.POST.getlist('choices-multiple-remove-button')
        num_skills = len(selected_skills)
        num_apps = regresionModel(selected_skills)
        num_apps = int(round(float(num_apps[0]),0))

        # because I need to pull data using a query that joins tables and runs an aggregate (to find number of matching skills per job adaptively),
        # I cannot map to the models and use a cursor object to link directly to the database. https://docs.djangoproject.com/en/dev/topics/db/sql/ <-- executing custom SQL directly
        cursor = connection.cursor()
        cursor.execute(MatchingAppsSQL(selected_skills)) # executes SQL query generated from MatchingAppsSQL function
        matching_apps = cursor.fetchall()

        context = {
            'selectedSkills': selected_skills,
            'numSkills': num_skills,
            'numApps': num_apps,
            'matchingApps' : matching_apps,
        }
        return render(request, 'employer/applicantlistings.html', context)
    return render(request, 'employer/applicantlistings.html')



def reviewApplicantsPageView(request):
    return render(request, 'employer/reviewapplicants.html')

def applicantProfilePageView(request):
    return render(request, 'employer/applicantprofile.html')

def postJobPageView(request):
    context = {"Skills": Skill.objects.all()}
    return render(request, 'employer/postjob.html', context)

def jobPostedPageView(request):
    if request.method == 'POST':
        new_job = Job()

        new_job.job_title = request.POST.get('job_title')
        new_job.salary = request.POST.get('salary')
        new_job.apply_startDate = request.POST.get('appStart')
        new_job.apply_endDate = request.POST.get('appEnd')
        new_job.job_startDate = request.POST.get('jobStart')
        new_job.job_location = request.POST.get('jobLoc')
        new_job.job_description = request.POST.get('jobDesc')
        new_job.job_requirements = request.POST.get('jobReq')
        new_job.relocation_package = request.POST.get('relocPac')
        new_job.job_benefits = request.POST.get('jobBen')
        new_job.Job_filled = False
        new_job.organization_id = Organization.objects.get(organization_id = 201)
        new_job.save()

        required_skills = request.POST.getlist('choices-multiple-remove-button-required')
        preferred_skills = request.POST.getlist('choices-multiple-remove-button-preferred')

        for skill in required_skills:
            new_job_skill = Job_Skill()
            new_job_skill.job_id = Job.objects.all().order_by("-job_id")[0]
            new_job_skill.skill_name = Skill.objects.get(skill_name = skill)
            new_job_skill.required = True
            new_job_skill.save()
        for skill in preferred_skills:
            new_job_skill = Job_Skill()
            new_job_skill.job_id = Job.objects.all().order_by("-job_id")[0]
            new_job_skill.skill_name = Skill.objects.get(skill_name = skill)
            new_job_skill.required = False
            new_job_skill.save()
        
    return render(request, 'employer/jobposted.html')

def editJobPageView(request):
    jobs = Job.objects.filter(organization_id_id = 201)
    context = {'Jobs' : jobs}
    return render(request, 'employer/editjob.html', context)

def editJobResponsePageView(request):
    job_to_edit = Job.objects.get(job_id = request.POST.get('choices-multiple-remove-button'))
    job_skills = Job_Skill.objects.filter(job_id= request.POST.get('choices-multiple-remove-button'))
    job_skills_req = []
    job_skills_pref = []
    for skill in job_skills:
        if skill.required == True:
            job_skills_req.append(skill.skill_name)
        else:
            job_skills_pref.append(skill.skill_name)

    context = {"jobToEdit" : job_to_edit,
               "jobIDToEdit" : request.POST.get('choices-multiple-remove-button'),
               "reqSkills" : job_skills_req,
               "prefSkills" : job_skills_pref,
               "Skills": Skill.objects.all(),}
    return render(request, 'employer/editjobresponse.html', context)

def editJobSuccessPageView(request):
    updated_job = Job.objects.get(job_id = request.POST.get('job_id'))
    old_skills = Job_Skill.objects.filter(job_id = request.POST.get('job_id'))
    old_skills.delete()
    print(f"Job ID: {request.POST.get('job_id')}")

    updated_job.job_id = request.POST.get('job_id')
    updated_job.job_title = request.POST.get('job_title')
    updated_job.salary = request.POST.get('salary')
    updated_job.apply_startDate = request.POST.get('appStart')
    updated_job.apply_endDate = request.POST.get('appEnd')
    updated_job.job_startDate = request.POST.get('jobStart')
    updated_job.job_location = request.POST.get('jobLoc')
    updated_job.job_description = request.POST.get('jobDesc')
    updated_job.job_requirements = request.POST.get('jobReq')
    updated_job.relocation_package = request.POST.get('relocPac')
    updated_job.job_benefits = request.POST.get('jobBen')
    
    if request.POST.get('deactivate') == 'True':
        updated_job.Job_filled = True
    else:
        updated_job.Job_filled = False
    updated_job.save()

    required_skills = request.POST.getlist('choices-multiple-remove-button-required')
    preferred_skills = request.POST.getlist('choices-multiple-remove-button-preferred')

    for skill in required_skills:
        new_job_skill = Job_Skill()
        new_job_skill.job_id = Job.objects.get(job_id=request.POST.get('job_id'))
        new_job_skill.skill_name = Skill.objects.get(skill_name = skill)
        new_job_skill.required = True
        new_job_skill.save()
    for skill in preferred_skills:
        new_job_skill = Job_Skill()
        new_job_skill.job_id = Job.objects.get(job_id=request.POST.get('job_id'))
        new_job_skill.skill_name = Skill.objects.get(skill_name = skill)
        new_job_skill.required = False
        new_job_skill.save()

    

    return render(request, 'employer/editjobsuccess.html')


def editEmployerProfilePageView(request):
    return render(request, 'employer/editemployerprofile.html')

def empMyAccountPageView(request):
    return render(request, 'employer/empmyaccount.html')

def MatchingAppsSQL(job_id, num_records = 10):
    
    query = f"""SELECT COUNT(has."skill_name_id"), has."user_id_id", ha."first_name", ha."last_name", ha."city", ha."state", ha."video_link", ha."resume_upload" FROM homepage_applicant_skill has
                INNER JOIN homepage_applicant ha ON ha."user_id" = has."user_id_id"
                WHERE has."skill_name_id" IN (SELECT hjs."skill_name_id" FROM homepage_job_skill hjs WHERE hjs."job_id_id" = {job_id})
                GROUP BY has."user_id_id", ha."first_name", ha."last_name", ha."city", ha."state", ha."video_link", ha."resume_upload"
                ORDER BY COUNT(has."skill_name_id") DESC
                LIMIT {num_records};"""
    return query

def regresionModel(selectedSkills):
    from urllib import request
    import urllib
    import json 

    num_skills = len(selectedSkills)
    regSkills = ["ai", "analytics", "collaboration", "desk", "e-commerce", "engineering", "html", "innovation", "lte", "presentation", "reporting"]

    val = ['0', num_skills]
    foundFlag = False

    for m in regSkills:
        for n in selectedSkills:
            if m == n:
                val.append('1')
                foundFlag = True
        if foundFlag == False:
            val.append('0')
        foundFlag = False

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["offer_count", "skill_count", "skill_ai", "skill_analytics", "skill_collaboration", "skill_desk", "skill_e-commerce", "skill_engineering", "skill_html", "skill_innovation", "skill_lte", "skill_presentation", "skill_reporting"],
                        "Values": [ val ]
                        },        },
                "GlobalParameters": {
        }
    }


    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/c387a78a702a4ce69af5f754b3333ae9/services/4ac159d291494dbb938621dd634eb1c4/execute?api-version=2.0&details=true'
    api_key = 'eRKWScvVRCaBdOFu7M4SQh/S1triyfplWgEr4eEkdDYY+H6E5eEBVkqEgc3DbexrrX+8QGY6z/tpBU4r351NWw=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)
    numApps = result['Results']['output1']['value']['Values'][0]

    return numApps



