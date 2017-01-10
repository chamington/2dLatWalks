def startsatend(x):#I know I can make it one line, but I don't care
    a=x.count('U')-x.count('D') #this calculates the total difference of hight
    b=x.count('R')-x.count('L') #Same for z
    return a==0 and b==0 #I'm not really sure what this does
def makeallsubsets(x): #Use this code if you want all subsets in a list, which is not needed a lot
    l = [] #So this declairs a list
    for j in range (1,len(x)+1): #So this does something, I forget. I'm not sure why this is len(x)+1. Usually it's len(x)-1
    	for i in range (0,len(x)-j+1): #I have no idea
    		l.append(x[i:i+j]) #There's going to be a lot to append
    return l



def makeallsubsetsAndCount(x):
    k=0
    for j in range (1,len(x)+1):
    	for i in range (0,len(x)-j+1):
    	        if startsatend(x[i:i+j]) == True:
                            k=k+1
    return k
