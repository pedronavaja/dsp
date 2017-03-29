##Q6:

import csv

with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')

    faculty_dict = { }

    faculty.next()

    for line in faculty:
        prof_name = line[0]
        name_list = prof_name.split()
        lastname = name_list[-1]
        position = line[2]
        title = position[:position.index('Professor')+9]
        data = [line[1],title,line[3]]
        if lastname not in faculty_dict:
            faculty_dict[lastname] = [data]
        else:
            faculty_dict[lastname] += [data]

    first_3_entries = {k: faculty_dict[k] for k in sorted(faculty_dict.keys())[:3]}
    print(first_3_entries)

##Q7:

import csv
with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')

    faculty_dict = { }

    faculty.next()

    for line in faculty:
        prof_name = line[0]
        name_list = prof_name.split()
        firstname = name_list[0]
        lastname = name_list[-1]
        full_name = (firstname, lastname)
        position = line[2]
        title = position[:position.index('Professor')+9]
        data = [line[1],title,line[3]]
        if full_name not in faculty_dict:
            faculty_dict[full_name] = [data]
        else:
            faculty_dict[full_name] += [data]

    first_3_entries = {k: faculty_dict[k] for k in sorted(faculty_dict.keys())[:3]}
    print(first_3_entries)

##Q8:

import csv
with open('faculty.csv') as csvfile:
    faculty = csv.reader(csvfile, delimiter = ',')

    faculty_dict = { }

    faculty.next()

    for line in faculty:
        prof_name = line[0]
        name_list = prof_name.split()
        firstname = name_list[0]
        lastname = name_list[-1]
        full_name = (firstname, lastname)
        position = line[2]
        title = position[:position.index('Professor')+9]
        data = [line[1],title,line[3]]
        if full_name not in faculty_dict:
            faculty_dict[full_name] = [data]
        else:
            faculty_dict[full_name] += [data]

    first_3_entries = {k: faculty_dict[k] for k in sorted(faculty_dict.keys(), key = lambda x: x[1])[:3]}
    print(first_3_entries)

