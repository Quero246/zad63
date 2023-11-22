data = []

def readFile(f):
    file = open(f, "r")
    dane = []
    for x in file:
        data.append(x.strip())

def zad2():
    readFile("ciagi.txt")
    ilos = 0
    for d in data:
        oneBefore = False
        git = True
        if d[0] == '1':
            oneBefore = True
        for i in range(1, len(d)):
            if oneBefore == True and d[i] == '1':
                git = False
                break
            elif d[i] == '1':
                oneBefore = True
            else:
                oneBefore = False
        
        if git == True:
            ilos += 1
            print(d)
    print(ilos)

zad2()
