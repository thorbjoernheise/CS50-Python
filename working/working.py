import re

def main():
    print(convert(input("Hours: ")))


def convert(s):

    # Using re to search for groups of needed data
    result = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if result:
        result = result.groups()

        # Assigning values
        start_hour = int(result[1])
        start_minute = int(0 if result[2] is None else result[2])
        end_hour = int(result[5])
        end_minute = int(0 if result[6] is None else result[6])

        # Error Handling
        if int(start_hour) > 12 or int(end_hour) > 12:
            raise ValueError
        if int(start_minute) >= 60 or int(end_minute) >= 60:
            raise ValueError

        # Handling PM
        if result[3] == "PM":
            start_hour = start_hour + 12
            if start_hour == 24:
                start_hour = 12
            if start_hour > 24:
                raise ValueError
        if result[7] == "PM":
            end_hour = end_hour + 12
            if end_hour == 24:
                end_hour = 12

        #Handling AM
        if result[3] == "AM" and start_hour == 12:
            start_hour = 00
        if result[7] == "AM" and end_hour == 12:
            end_hour = 00

        #building the formated string
        formated = (f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}")
        return formated
    else:
        raise ValueError

if __name__ == "__main__":
    main()




