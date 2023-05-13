def main():
    original_tweet = input("Input:")
    print("Output:", converter(original_tweet))

def converter(original_tweet: str) -> str:
    for c in original_tweet:
        c = c.casefold()
        if c in ("a", "e", "i", "o", "u" ):
            original_tweet = original_tweet.replace(c.upper(), "").replace(c.lower(), "")
    return original_tweet

if __name__ == "__main__":
    main()

