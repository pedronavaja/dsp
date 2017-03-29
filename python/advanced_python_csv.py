import csv
import re

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')


    faculty_emails = []

    faculty.next()

    for line in faculty:
        email = re.match(r'[\w\.-]+@[\w\.-]+', line[3])

        faculty_emails.append(email.group(0))

with open('emails_regex.csv', 'w') as newcsv:
    emailwriter = csv.writer(newcsv, delimiter = ',')

    for email in faculty_emails:
        emailwriter.writerow([email])
