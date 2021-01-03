def translator(phrase):
    new = ""
    for i in phrase:
        if i.upper() in "AEIOU":
            if i.isupper():
                new = new + "G"
            else:
                new = new + "g"
        else:
            new = new + i
    return new

phrase = str(input("Enter a phrase : "))
print(translator(phrase))
