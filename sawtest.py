import walkgraphics
import crosscounter
import sequentialWalk
import turtle
turtle.penup()
turtle.sety(-300)
turtle.setx(600)
turtle.pendown()
for i in range(1,100000):
    j=sequentialWalk.nthWalk(i)
    #if crosscounter.makeallsubsetsAndCount(j)==0:
    walkgraphics.walkVisualiser(j)
        #print(j)
        #print(i)
        #print
