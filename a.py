#!/usr/bin/python

import csv
import templates

def g():
  return generateApplications()

def generateApplications():
  reader = csv.reader(open('r.csv', 'rb'))
  fields = []
  for applicant in reader:
    if len(fields) == 0:
      fields = applicant
    else:
      buildApplicationForm(fields, applicant)
  return

def normalizeData(fields, data):
  payload = []
  payload.append(normalizePersonal(data[0:10]))
  payload.append(normalizeActivites(data[10:52]))
  payload.append(normalizeActivites(data[52:]))
  return payload

def normalizePersonal(data):
  return {  'time':data[0],
            'name':data[1],
            'id':data[2],
            'grade':data[3],
            'fourthTeacher':data[4],
            'fourthRoom':data[5],
            'email':data[6],
            'homePhone':data[7],
            'cellPhone':data[8],
            'gpa':data[9] }

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

def normalizeActivites(data):
  p = []
  for a in lol(data,7):
    p.append(normalizeActivity(a))
  return p

def normalizeActivity(data):
  fields = ['name', 'desc', 'hours', 'date', 'sName', 'sPhone', 'sEmail']
  return buildDictionary(fields, data)

def buildDictionary(fields, data):
  p = dict()
  if len(data) != len(fields):
    print("field and data length did not match!!!!")
    return
  for i, f in enumerate(fields):
    p[f] = data[i]
  return p


def buildApplicationForm(fields, data):
  p = normalizeData(fields,data)
  fileName = p[0]['name'] + '.html'
  file = open('applications/' + fileName, 'w+')
  file.write("<!DOCTYPE html> <html lang='en'>")
  file.write("<link rel='stylesheet' type='text/css' href='assets/css/bootstrap.min.css'>")
  file.write("<h1>Personal Information</h1>")
  file.write(templates.personalInfoTemplate.substitute(p[0]))
  leadershipTemplates = [];
  for x in p[1]:
    leadershipTemplates.append(templates.activityTemplate.substitute(x))
  file.write("<h1>Leadership Activities</h1>")
  file.write(templates.activitiesTemplate.substitute(activity1=leadershipTemplates[0],
                                           activity2=leadershipTemplates[1],
                                           activity3=leadershipTemplates[2],
                                           activity4=leadershipTemplates[3],
                                           activity5=leadershipTemplates[4],
                                           activity6=leadershipTemplates[5]))
  serviceTemplates = [];
  for x in p[2]:
    serviceTemplates.append(templates.activityTemplate.substitute(x))
  file.write("<h1>Service Activities</h1>")
  file.write(templates.activitiesTemplate.substitute(activity1=serviceTemplates[0],
                                           activity2=serviceTemplates[1],
                                           activity3=serviceTemplates[2],
                                           activity4=serviceTemplates[3],
                                           activity5=serviceTemplates[4],
                                           activity6=serviceTemplates[5]))
  file.write("</html>")
  file.close()
