import sys
import csv

def main():
    file_input = sys.argv[1]
    file_output = sys.argv[2]
    validate(file_input)
    format(file_input, file_output)

def validate(path):

    #Validation and Error handling
    a, b = path.split(".")
    if b != "csv":
        sys.exit("Not a CSV file")
    try:
        with open(path) as file:
            pass
    except FileNotFoundError:
        sys.exit(f"Could not read {path}")

def format(file_input, file_output):
    students = []

    #Reading the input file
    with open(file_input) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names = row['name'].split(', ')
            firstName = names[1]
            lastName = names[0]
            house = row['house']
            students.append({'first': firstName, 'last': lastName, "house": house})

    #Writing the to the output path
    keys = students[0].keys()
    with open(file_output, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    main()
