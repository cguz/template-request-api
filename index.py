import sys
import requests
import json

TEMPLATE_URL="http://gedapvl395.a.space.corp:5000/api/rawbookings/totals"

if len(sys.argv) < 2:
    print("Please provide the ticket file as input")
    sys.exit()

file_path = str(sys.argv[1])

print("File name {}".format(file_path))

# reading file line by line 
file1 = open(file_path, "r")
lines = file1.readlines()

# creating the headers
headers = {
    'accept' : 'application/json',
}

# for each content of the file
for line in lines:

    # creating the API call 

    # creating the params
    params = {
        'comment' : line.strip(),
    }

    response = requests.get(TEMPLATE_URL, params=params, headers=headers)

    if response.status_code == 200:
        # print("request link: {} {} {}".format(TEMPLATE_URL, params, headers))
        # print(response.json())
        # example json: [{'team': [{'totalHours': 2.5, 'userName': 'Cesar'}], 'ticketId': 'COSGS-902', 'totalHours': 2.5}]
        booking = json.loads(json.dumps(response.json()))[0]
        # print(booking)
        print("Ticket ID {} spent {} total hours".format(booking["ticketId"], booking["totalHours"]))
        for t in booking["team"]:
            print(" {} : {}".format(t["userName"], t["totalHours"]))


# curl -X 'GET' 'http://gedapvl395.a.space.corp:5000/api/rawbookings/totals?comment=COS' -H 'accept: application/json'
