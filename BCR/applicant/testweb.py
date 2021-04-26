def SkillRecommender(current_skill):
    from urllib import request
    import urllib
    # If you are using Python 3+, import urllib instead of urllib2

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
    api_key = 'Ly1D5fsPIztYYP1he6Xv8LEqv0nVnQZf9I/WB/UahbiNuNpJK1qQuCHVFK7T9hg9MszoO6cuLcBDTAxnxWWXhg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)
    rec_skills = result['Results']['output1']['value']['Values'][0]
    rec_skills.pop(0)
    return rec_skills
