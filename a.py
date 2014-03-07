#!/usr/bin/python

import csv
import subprocess
import templates

# Development, clear and rebuild applications
def d():
  _clearApplications()
  generateApplications()

# Alias for clearApplications()
def c():
  return clearApplications()

# Removes all the applications in the applications directory
def clearApplications():
  decision = raw_input("Are you sure you want to remove applications? yn ")
  if decision in ['Y', 'y']:
    _clearApplications() 
    print "Removed"
  else:
    print "Cancelled"
  return  

def _clearApplications():
  subprocess.call("rm applications/*.html", shell=True)


# Alias for generateApplications()
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

def buildPersonalInformation(info):
  return templates.personalInfoTemplate.substitute(info)

def buildActivities(activities):
  activityTemplates = []
  for x in activities:
    activityTemplates.append(templates.activityTemplate.substitute(x))
  return templates.activitiesTemplate.substitute(activity1=activityTemplates[0],
                                           activity2=activityTemplates[1],
                                           activity3=activityTemplates[2],
                                           activity4=activityTemplates[3],
                                           activity5=activityTemplates[4],
                                           activity6=activityTemplates[5])


def buildApplicationForm(fields, data):
  p = normalizeData(fields,data)
  fileName = p[0]['name'] + '.html'
  file = open('applications/' + fileName, 'w+')
  file.write(templates.applicationTemplate.substitute(personalInformation=buildPersonalInformation(p[0]),
                                                      leadershipActivities=buildActivities(p[1]),
                                                      serviceActivities=buildActivities(p[2])))
  file.close()
