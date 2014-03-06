
from string import Template

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
