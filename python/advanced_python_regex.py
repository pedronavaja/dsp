##Q1 CODE
import csv
import re

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')

    degree_freqs = { }
    degrees = []
    multiples = []

    faculty.next()

    for line in faculty:
        quals = line[1]
        degree = quals.strip()
        degree = re.sub(r'\.', "", degree)
        if len(degree) > 3:
            multidegree = degree.split()
            for item in multidegree:
                multiples.append(item)
        else:
            degrees.append(degree)
    degrees.extend(multiples)

    for degree in degrees:
        if degree not in degree_freqs:
            degree_freqs[degree] = 1
        else:
            degree_freqs[degree] += 1



    print("The number of different degrees is: " + str(len(degree_freqs)))
    print(degree_freqs)

##Q2 Answers

import csv

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')

    type_freqs = { }
    faculty_type = []

    faculty.next()

    for line in faculty:
        position = line[2]
        position_type = position[:position.index('Professor')+9]
        faculty_type.append(position_type)

    for position in faculty_type:
        if position not in type_freqs:
            type_freqs[position] = 1
        else:
            type_freqs[position] += 1



    print("The number of different faculty types is: " + str(len(type_freqs)))
    print(type_freqs)

##Q3

import csv

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')


    faculty_emails = []

    faculty.next()

    for line in faculty:
        email = line[3]

        faculty_emails.append(email)



    print(faculty_emails)

##Q4

import csv

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')


    email_domains = []
    unique_domains = []

    faculty.next()

    for line in faculty:
        email = line[3]
        domain = email[email.index('@'):]
        email_domains.append(domain)

    for domain in email_domains:
        if domain not in unique_domains:
            unique_domains.append(domain)

    print("The number of unique email domains is " + str(len(unique_domains)))
    print(unique_domains)

