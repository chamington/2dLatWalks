def startsatend(x):#I know I can make it one line, but I don't care
    a=x.count('U')-x.count('D')
    b=x.count('R')-x.count('L')
    return a==0 and b==0
def makeallsubsets(x): #Use this code if you want all subsets in a list, which is not needed a lot
    l = []
    for j in range (1,len(x)+1):
    	for i in range (0,len(x)-j+1):
    		l.append(x[i:i+j]) #There's going to be a lot to append
    return l



def makeallsubsetsAndCount(x):
    k=0
    for j in range (1,len(x)+1):
    	for i in range (0,len(x)-j+1):
    	        if startsatend(x[i:i+j]) == True:
                            k=k+1
    return k
