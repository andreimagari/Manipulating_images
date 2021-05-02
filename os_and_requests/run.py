#! /usr/bin/env python3

import os
import requests

IP_Address = '34.122.185.236'
feedbackDir = '/data/feedback/'
feedbackFiles = os.listdir(feedbackDir)

for f in feedbackFiles:
    fb = open(feedbackDir+f)
    data = fb.read().split('\n')
    dict = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
    reponse = resquests.post('https://{}/feedback/' .format(IP_Address), json=dict)
    print(response.status_code)


