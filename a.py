#!/usr/bin/python

import csv
from string import Template


# map = ['Timestamp', 'Full Name', 'Student ID #', 'Grade', 'Fourth Period Teacher', 'Fourth Period Teacher Room #', 'Your email address', 'Your Home Phone #', 'Your cell phone (if available)', 'Your current cumulative GPA (weighted)', 'Activity Name', 'Description of Accomplishment', 'Total Hours', 'Date Performed', 'Supervisor Name', 'Supervisor Email', 'Activity Name', 'Description of Accomplishment', 'Total Hours', 'Date Performed', 'Supervisor Name', 'Supervisor Phone #', 'Supervisor Email', 'Activity Name', 'Description of Accomplishment', 'Date Performed', 'Supervisor Name', 'Supervisor Phone #', 'Supervisor Email', 'Activity Name', 'Description of Accomplishment', 'Total Hours', 'Date Performed', 'Supervisor Name', 'Supervisor Phone #', 'Supervisor Email', 'Activity Name', 'Description of Accomplishment', 'Total Hours', 'Date Performed', 'Supervisor Name', 'Supervisor Phone #', 'Supervisor Email', 'Activity Name', 'Description of Accomplishment', 'Total Hours', 'Date Performed', 'Supervisor Name', 'Supervisor Phone #', 'Supervisor Email']

# Iterate over the csv file and call buildApplicationForm with dictionaryObject
def g():
  reader = csv.reader(open('r.csv', 'rb'))
  fields = []
  for applicant in reader:
    if len(fields) == 0:
      fields = applicant
    else:
      buildApplicationForm(fields, applicant)
  return

personalInfoTemplate = Template("""
  <p>Full Name: $name</p>
  <p>Student ID #: $id</p>
  <p>Grade: $grade</p>
  <p>Fourth Period Teacher: $fourthTeacher</p>
  <p>Fourth Period Room Number: $fourthRoom</p>
  <p>Email Address: $email</p>
  <p>Home Phone: $homePhone</p>
  <p>Cell Phone: $cellPhone</p>
  <p>GPA: $gpa</p>
  """)

activitiesTemplate = Template("""
  <table class='table'>
  <thead>
    <tr> 
      <th>Name</th>
      <th>Description</th>
      <th>Hours</th>
      <th>Date</th>
      <th>Supervisor Name</th>
      <th>Supervisor Phone Number</th>
      <th>Supervisor Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      $activity1
    </tr>
    <tr>
      $activity2
    </tr>
    <tr>
      $activity3
    </tr>
    <tr>
      $activity4
    </tr>
    <tr>
      $activity5
    </tr>
    <tr>
      $activity6
    </tr>
  </tbody>
  </table>
  """)

activityTemplate = Template("""
    <td> $name
    </td>
    <td> $desc
    </td>
    <td>$hours
    </td>
    <td>$date
    </td>
    <td>$sName
    </td>
    <td>$sPhone
    </td>
    <td>$sEmail
    </td>
  """)

activityTemplate1 = Template("""
    $name on $date for $hours hours
    <p>$desc</p>
    <p>Supervisor Name: $sName  Phone Number: $sPhone  Email: $sEmail</p>
  """)

activitiesTemplate1 = Template("""
    $activity1
    $activity2
    $activity3
    $activity4
    $activity5
    $activity6
  """)


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
  file.write(personalInfoTemplate.substitute(p[0]))
  templates = [];
  for x in p[1]:
    templates.append(activityTemplate.substitute(x))
  file.write("<h1>Leadership Activities</h1>")
  file.write(activitiesTemplate.substitute(activity1=templates[0],
                                           activity2=templates[1],
                                           activity3=templates[2],
                                           activity4=templates[3],
                                           activity5=templates[4],
                                           activity6=templates[5]))
  templates = [];
  for x in p[2]:
    templates.append(activityTemplate.substitute(x))
  file.write("<h1>Service Activities</h1>")
  file.write(activitiesTemplate.substitute(activity1=templates[0],
                                           activity2=templates[1],
                                           activity3=templates[2],
                                           activity4=templates[3],
                                           activity5=templates[4],
                                           activity6=templates[5]))
  file.write("</html>")


  file.close()
