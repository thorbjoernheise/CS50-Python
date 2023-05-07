def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #No Punctuation
    if any(c in " .,!?" for c in s):
        return False

    #Length between 2 and 4
    if len(s) < 2 or len(s) > 6:
        return False

    #First two must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    #Numbers can't be in the middle
    if any(c.isnumeric() for c in s):
        for i in range(len(s)):
            if s[i].isdigit():
                for j in range(i+1, len(s)):
                    if not s[j].isdigit():
                        return False


    #check if the first digit is a zero
    first_digit = False
    for c in s:
        if c.isdigit():
            if not first_digit:
                first_digit = True
                if c == "0":
                    return False
            break
    return True


if __name__ == "__main__":
    main()




