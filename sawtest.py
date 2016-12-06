def startsatend(x):
	a=x.count('U')-x.count('D')
	b=x.count('R')-x.count('L')
	if a==0 and b==0:
		return True
	else:
		return False
def makeallsubsets(x):
	l = []
	for j in range (1,len(x)+1):
		for i in range (0,len(x)-j+1):
			l.append(x[i:i+j])
	return l

def crossCount(x):
	k=0
	for i in range (0,len(makeallsubsets(x))):
		if startsatend((makeallsubsets(x)[i])) == True:
			k=k+1
	return k

def makeallsubsetsAndCount(x):
        k=0
	for j in range (1,len(x)+1):
		for i in range (0,len(x)-j+1):
		        if startsatend(x[i:i+j]) == True:
                                k=k+1
	return k


"""
x=raw_input("Give a walk: ")
x=str(x)
if x.count("U")+x.count("D")+x.count("L")+x.count("R") != len(x):
        print("This is not a valid walk, a valid walk only consists of U for up, D for down, L for left, and R for right")
        os.execl(sys.executable, sys.executable, *sys.argv)
else:
        y=makeallsubsetsAndCount(x)
        if y==0:
                print("Yes, it walked over an existing path 0 times")
        else:
                print("No, it crossed itself "+str(y)+" times")
"""
