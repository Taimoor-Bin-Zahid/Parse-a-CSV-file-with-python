import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['rank', 'discipline', 'phd', 'service', 'sex']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['salary']
            csv_writer.writerow(line)



############################## for reading each value in a dictionary ############################
    # csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line)
############################## for reading each value in a dictionary ############################





############################## for creating a new CSV File #######################################
    # with open('new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='-')

    #     for line in csv_reader:
    #         csv_writer.writerow(line)
############################## for creating a new CSV File #######################################
