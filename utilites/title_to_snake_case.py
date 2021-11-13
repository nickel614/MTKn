
def titleToSnakeCase(string):
    newString = ''
    for i, e in enumerate(iterable=string, start=1):
        if e.isupper():
            newString = newString + '_'
        newString = newString + e.lower()

    return(newString[1:])
