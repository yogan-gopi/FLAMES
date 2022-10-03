def printRelation(f):
    global name1, name2
    prompt = "The Relationship between {} and {} will end in ".format(name1, name2)
    if f == "F":
        print(prompt+"FRIENDS!")
    elif f == "L":
        print(prompt+"LOVE!")
    elif f == "A":
        print(prompt+"AFFECTION!")
    elif f == "M":
        print(prompt+"MARRIAGE!")
    elif f == "E":
        print(prompt+"ENEMY!")
    else:
        print(prompt+"SIBLINGS!")

def calculateRelation(name1, name2):
    f  =['F', 'L', 'A', 'M', 'E', 'S']
    fLen = len(f)
    name1 = name1.lower()
    name2 = name2.lower()
    name1.replace(" ", "")
    name2.replace(" ", "")

    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(i, "", 1)

    n = len(name1) + len(name2)
    i = 0

    for _ in range(fLen-2):
        for x in range(n):
            i = ((i+1) % fLen)
        f.pop(i)
    return f[0]
    

if __name__ == '__main__':

    name1 = input("Enter Your Name: ")
    name2 = input("Enter Your Crush Name: ")

    relation = calculateRelation(name1, name2)
    printRelation(relation)
