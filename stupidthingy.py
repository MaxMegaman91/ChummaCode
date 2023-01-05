import math

ilist = [10, 90, 50, 90, 10, 90, 50, 90]

def move(mousepointer, length, heading):
	mousepointer[0] += round(length * math.cos(math.radians(heading)), 2)
	mousepointer[1] += round(length * math.sin(math.radians(heading)), 2)

	return tuple(mousepointer)

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def tracking(inputlist):
    mousepointer = [0,0]
    pointlist = [(0,0)]
    heading = 0

    for x in range(0,len(inputlist),2):
        pointlist.append(move(mousepointer, inputlist[x], heading))
        heading += inputlist[x+1]
        #print(pointlist)
    
    return pointlist
	# print(heading)

def area(pointlist):
    templist = []
    for x in range(0,len(pointlist)-1):
        templist.append(pointlist[x][0]*pointlist[x+1][1] - pointlist[x][1]*pointlist[x+1][0])
    return round(abs(sum(templist)/2))

print(area(tracking(ilist)))
#print(distance([0,0],[1,1]))