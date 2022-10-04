class Flames:   

    relations = {'F': "FRIENDS!", 'L': "LOVE!", 'A': "AFFECTION!", 'M': "MARRIAGE!", 'E': "ENEMY", 'S': "SISTERS!"}
    f  =['F', 'L', 'A', 'M', 'E', 'S']
    
    def __init__(self, name1 = "", name2 = ""):

        if name1 == name2 == "":
            self.name1 = input("Enter Your Name: ")
            self.name2 = input("Enter Your Crush Name: ")
        else:
            self.name1 = name1
            self.name2 = name2
        
        self.relation = self.calculateRelation()
        self.printRelation()

    def printRelation(self): # To Display the relationship

        self.prompt = "The Relationship between {} and {} will end in {}".format(self.name1 , self.name2, Flames.relations[self.relation])
        print(self.prompt)
        
    def calculateRelation(self): # To find the relationship between name1 and name2
        
        n1 = self.name1.lower().rstrip().replace(" ", "")
        n2 = self.name2.lower().rstrip().replace(" ", "")
        
        for i in n1:
            if i in n2:
                n1 = n1.replace(i, "", 1)
                n2 = n2.replace(i, "", 1)

        n = len(n1) + len(n2)
        i = 0

        for _ in range(5):
            i -= 1
            fLen = len(Flames.f)
            for x in range(n):
                i = ((i+1) % fLen)
            Flames.f.pop(i)
        return Flames.f[0]
    

if __name__ == '__main__':

    Flames()
