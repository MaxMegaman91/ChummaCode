# https://edabit.com/challenge/YDgtdP69Mn9pC73xN
# No edits allowed

def num_grid(minelist):
    listofhshx = []
    listofhshy = []

    def setnear(x,y):
        for i in range(-1, 2):
            for j in range(-1,2):
                if (x+i>=0 and x+i<5) and (y+j>=0 and y+j<5):
                    if minelist[x+i][y+j] == "0":
                        minelist[x+i][y+j] = str(0)
                    if minelist[x+i][y+j] == "#":
                        continue
                    minelist[x+i][y+j] = str(int(minelist[x+i][y+j]) + 1)




    for x in range(0,5):
        for y in range(0,5):
            if minelist[x][y] == "#":
                listofhshx.append(x)
                listofhshy.append(y)
            elif minelist[x][y] == "-":
                minelist[x][y] = "0"

    for index in range(0,len(listofhshx)):
        setnear(listofhshx[index],listofhshy[index])

    return minelist

