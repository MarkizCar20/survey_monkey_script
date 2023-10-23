#!/usr/bin/env python3

#Script for creating Survermonkey survey based on a json file containing questions and answers.

import requests
import json

API_URL = "https://api.surveymonkey.com/v3"

ACCESS_TOKEN = "rJOLXwrwqRRUrgYpqlqDVEPEyOdVFhrLzGOKCTGwiisgkuHx0WTXDPDTbalnDauXAOh.yv2m1Y6RXL762pggAbIu.YhaDJTFZOutrTA86s6sIiA4y8mSRGV.wgkVjLh4"

with open("./surveys/questions.json", "r") as json_file:
    questions = json.load(json_file)

with open("./emails.txt", "r") as email_file:
    email_addresses = email_file.read().splitlines()

#Create survey function
def create_survey():
    headers = {
        "Authorization":f"Bearer {ACCESS_TOKEN}",
        "Content-type": "application/json",
    }
    survey_data = {
        "title": "Survey generator test",
        "nickname": "surv_test",
    }
    response = requests.post(f"{API_URL}/surveys", headers = headers, json=survey_data)
    survey_id = response.json()["id"]
    return survey_id


if __name__ == "__main__":
    survey_id = create_survey()
    print(f"{survey_id}")