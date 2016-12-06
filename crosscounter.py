def startsatend(x):#I'm sure I can remove the ifs but I'm not sure how
    a=x.count('U')-x.count('D')
    b=x.count('R')-x.count('L')
    if a==0 and b==0:
    	return True
    else:
    	return False
def makeallsubsets(x): #Use this code if you want all subsets in a list, which is not needed a lot
    l = []
    for j in range (1,len(x)+1):
    	for i in range (0,len(x)-j+1):
    		l.append(x[i:i+j]) #There's going to be a lot to append
    return l

def crossCount(x): #Don't use this code, it is inefficient in terms of time and memory
    k=0
    for i in range (0,len(makeallsubsets(x))):
    	if startsatend((makeallsubsets(x)[i])) == True:
    		k=k+1
    return k

#vv USE THIS CODE startsatend(x) and crossCount(x) is only kept because I don't like deleting things


def makeallsubsetsAndCount(x):
    k=0
    for j in range (1,len(x)+1):
    	for i in range (0,len(x)-j+1):
    	        if startsatend(x[i:i+j]) == True:
                            k=k+1
    return k
