from django.shortcuts import render
from .models import Skill, Applicant_Skill
from django.db import connection

# Create your views here.
def employerPageView(request):
    return render(request, 'employer/index.html')

def findApplicantsPageView(request):
    return render(request, 'employer/findapplicants.html')

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


def reviewApplicantsPageView(request):
    return render(request, 'employer/reviewapplicants.html')

def applicantProfilePageView(request):
    return render(request, 'employer/applicantprofile.html')

def postJobPageView(request):
    return render(request, 'employer/postjob.html')

def editEmployerProfilePageView(request):
    return render(request, 'employer/editemployerprofile.html')

def MatchingAppsSQL(skill_names, num_records = 10):
    skills_sql_format = "'"
    for skill in skill_names:
        skills_sql_format += skill + "', '"
    skills_sql_format = skills_sql_format[:-1]
    skills_sql_format = skills_sql_format[:-1]
    skills_sql_format = skills_sql_format[:-1]
    query = f"""SELECT COUNT(has."skill_name") AS Matching_Skills, a."user_id", (a."first_name" + " " + a."lastname") AS Applicant_Name, a."city", '' AS video_button FROM homepage_applicant_skill has
                INNER JOIN homepage_applicant a ON has."user_id" = a."user_id"
                WHERE has."skill_name" IN ({skills_sql_format}) AND a."seeking_work" != True
                GROUP BY has."user_id", a."first_name", a."last_name", a."city"
                HAVING COUNT(has."skill_name") > 0
                ORDER BY COUNT(has."skill_name") DESC
                LIMIT {num_records}"""
    return query





