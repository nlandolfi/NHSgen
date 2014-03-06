#!/usr/bin/python

import csv
import templates

# Alias for generateApplications
def g():
  return generateApplications()

'''
  Main static function, reads "r.csv" and
  spits out html files in applications/
'''
def generateApplications():
  reader = csv.reader(open('r.csv', 'rb'))
  fields = []
  for applicant in reader:
    if len(fields) == 0:
      fields = applicant
    else:
      buildApplicationForm(fields, applicant)
  return

'''
 Returns payload of three arrays:
  - Personal Information Hash
  - Leadership Activities (Array of Hashes)
  - Service Activities (Array of Hashes)
'''
def normalizeData(fields, data):
  payload = []
  payload.append(normalizePersonal(data[0:10]))
  payload.append(normalizeActivites(data[10:52]))
  payload.append(normalizeActivites(data[52:]))
  return payload

# Returnes hash of personal info
def normalizePersonal(data):
  fields = ['time', 'name', 'id', 'grade', 'fourthTeacher', 'fourthRoom', 'email', 'homePhone', 'cellPhone', 'gpa']
  return buildHash(fields, data)

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

# Takes a long list of activites --> array of activity hashes
def normalizeActivites(data):
  activities = []
  for activity in lol(data,7):
    activities.append(normalizeActivity(activity))
  return activities

# Takes list of activity attrs --> activity hash
def normalizeActivity(data):
  fields = ['name', 'desc', 'hours', 'date', 'sName', 'sPhone', 'sEmail']
  return buildHash(fields, data)

# Takes an array of fields and array of values
def buildHash(fields, data):
  return dict(zip(fields,data))


def buildApplicationForm(fields, data):
  payload = normalizeData(fields,data)
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
