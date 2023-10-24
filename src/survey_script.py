#!/usr/bin/env python3

#Script for creating Survermonkey survey based on a json file containing questions and answers.

from wsgiref import headers
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

def create_questions(survey_id):
    headers = {
        "Authorization":f"Bearer {ACCESS_TOKEN}",
        "Content-Type":"application/json",
    }
    for page_name, page_data in questions["Survey Name"].items():
        for question_name, question_data in page_data.items():
            question_data["type"] = "multiple_choice"
            data = {
                "title": question_name,
                "family": question_data["type"],
                "subtype": "vertical",
                "headings": [{"heading": page_name}],
                "position": 1,
                "description": question_data["Description"],
                "answers": [{"text": answer} for answer in question_data["Answers"]],
            }
            response = requests.post(f"{API_URL}/surveys/{survey_id}/pages/1/questions", headers=headers, json=data)
            print(f"Created question: {question_name}")

def send_invitations(survey_id):
    headers = {
        "Authorization":f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    recepient_data = [{"email": email, "first_name": "", "last_name": ""} for email in email_addresses]
    data = { "recepients":recepient_data, "type":"email"}
    response = requests.post(f"{API_URL}/surveys/{survey_id}/collectors", headers=headers, json=data)
    print(f"{response}")
    print(response.content)

if __name__ == "__main__":
    survey_id = create_survey()
    print(f"{survey_id}")
    create_questions(survey_id)
    send_invitations(survey_id)