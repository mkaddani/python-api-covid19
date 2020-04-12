#+-------------------+
#| MKADDANI          |
#| PYTHON - COVID19  |
#| -- API            |
#| |>unfinished      |
#+-------------------+
# run by using python3.7 script.py


import requests

import json

response = requests.get("https://api.covid19api.com/total/country/morocco/status/confirmed")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)

jprint(response.json())


#text = json.dumps(response.json(), sort_keys=True, indent=4)

#input_dict = json.loads(text)

#output_dict = [x for x in input_dict if x['Country'] == 'Morocco']

#output_json = json.dumps(output_dict)

#print(output_json)



