from django.shortcuts import render
from .models import Skill, Applicant_Skill
from django.db import connection

# Create your views here.

def applicantPageView(request):
    return render(request, 'applicant/index.html')

def findAJobPageView(request):
    context = {"Skills": Skill.objects.all()}

    return render(request, 'applicant/findajob.html', context)

def jobListingsPageView(request):
    if request.method == 'POST':
        selected_skills = request.POST.getlist('choices-multiple-remove-button')
        num_skills = len(selected_skills)
        num_jobs = regresionModel(selected_skills)
        num_jobs = int(round(float(num_jobs[0]),0))

        # because I need to pull data using a query that joins tables and runs an aggregate (to find number of matching skills per job adaptively),
        # I cannot map to the models and use a cursor object to link directly to the database. https://docs.djangoproject.com/en/dev/topics/db/sql/ <-- executing custom SQL directly
        cursor = connection.cursor()
        cursor.execute(MatchingJobsSQL(selected_skills)) # executes SQL query generated from MatchingJobsSQL function
        matching_jobs = cursor.fetchall()

        context = {
            'selectedSkills': selected_skills,
            'numSkills': num_skills,
            'numJobs': num_jobs,
            'matchingJobs' : matching_jobs,
        }
        return render(request, 'applicant/joblistings.html', context)
    return render(request, 'applicant/joblistings.html')


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
    numJobs = result['Results']['output1']['value']['Values'][0]

    return numJobs
    

def jobDetailsPageView(request):
    return render(request, 'applicant/jobdetails.html')

def companyProfilePageView(request):
    return render(request, 'applicant/companyprofile.html')

def skillRecommenderPageView(request):
    return render(request, 'applicant/skillrecommender.html')

def offersPageView(request):
    return render(request, 'applicant/offers.html')

def skillRecommenderResponsePageView(request):

    if request.method == 'POST':
        skill = request.POST['skill']
        SkillsReturned = SkillRecommender(skill)
        context = {'SkillsReturned' : SkillsReturned}
        return render(request, 'applicant/skillrecommenderresponse.html', context)

    return render(request, 'applicant/skillrecommender.html')

def SkillRecommender(current_skill):
    from urllib import request
    import urllib

    import json 


    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["user_id", "skill_id", "offer_count"],
                        "Values": [ [ "0", current_skill, "0" ],]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0bb233f06aa1452aae79ada1b7f6f7c0/services/bbebdc8c03244a4e9e90ab719cfcc1a4/execute?api-version=2.0&details=true'
    api_key = 'Ly1D5fsPIztYYP1he6Xv8LEqv0nVnQZf9I/WB/UahbiNuNpJK1qQuCHVFK7T9hg9MszoO6cuLcBDTAxnxWWXhg=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)
    rec_skills = result['Results']['output1']['value']['Values'][0]
    rec_skills.pop(0)
    return rec_skills

def MatchingJobsSQL(skill_names, num_records = 10):
    skills_sql_format = "'"
    for skill in skill_names:
        skills_sql_format += skill + "', '"
    skills_sql_format = skills_sql_format[:-1]
    skills_sql_format = skills_sql_format[:-1]
    skills_sql_format = skills_sql_format[:-1]
    query = f"""SELECT COUNT(hjs."skill_name") AS Matching_Skills, hjs."job_id", hj."job_title", ho."company_name", hj."job_location", '' AS video_button FROM homepage_job_skill hjs
                INNER JOIN homepage_job hj ON hj."job_id" = hjs."job_id"
                LEFT OUTER JOIN homepage_organization ho ON ho."organization_id" = hj."organization_id"
                WHERE hjs."skill_name" IN ({skills_sql_format}) AND hj."Job_filled" != True
                GROUP BY hjs."job_id", hj."job_title", ho."company_name", hj."job_location"
                HAVING COUNT(hjs."skill_name") > 0
                ORDER BY COUNT(hjs."skill_name") DESC
                LIMIT {num_records}"""
    return query

