import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    #Using the /embed/ as left and the " as right boundary
    result = re.search(r'\/embed\/(.+?)"', s)
    if result:
        #adding the found result to the link 
        url = f"https://youtu.be/{result.group(1)}"
        return url


if __name__ == "__main__":
    main()
