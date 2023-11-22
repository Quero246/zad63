def readFile(f):
    file = open(f, "r")
    dane = []
    for x in file:
        dane.append(int(x.strip()))
    return(dane)
