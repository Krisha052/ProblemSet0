
def main():
    phrase = input("What was that? ")
    print(convert(phrase))

def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase


if __name__ == "__main__":
    main()