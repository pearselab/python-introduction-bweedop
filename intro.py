
#problem_1
for i in range(20,9,-1):
    print(i)

#problem_2
x=[i for i in range (20,9,-1)]
print(x)

#problem_3
for i in range(20,9,-2):
    print(i)

#problem_4
x=[i for i in range (20,9,-2)]
print(x)

#problem_5
def prime(num):
    if  num<1:
        print("Numbers less than one are not prime")
    for i in range(2,num):
        if (num%i) > 0:
            print(num,"is a prime number")
            break
        else:
            print(num,"is not a prime number")
            break
prime(num=7)

#problem_6
lines=[]
with open("nights_watch.txt") as handle:
    for chars in handle:
        lines.append(chars[4])
print(lines[4])

#problem_7

for i in range(0,20,1):
    if i <2:
        pass
    elif i%5==0:
        print("Good:", i)
    elif all(i%j!=0 for j in range(2,i)):
            print("Job:", i)
    else:
        pass

#problem_8

def gomp(t,a,b,c):
    e=2.71828
    return(int(a*e**(-b*e**(-c*t))))
print(gomp(t=8,a=10,b=-0.5,c=-0.3))
    
#problem_9
def stars(ht,wd):
    for i in range(0,ht):
        if i ==0:
            print("*"*wd)
        elif i < ht-1:
            print("*" + " "*wd + "*")
        else:
            print("*"*wd)
stars(ht=5,wd=5)

#problem_10

class Point:
    def __init__(self, xcor, ycor):
        self.xcor, self.ycor= xcor, ycor
    ####problem_11
    def distance (self,p2):
        dist=((self.xcor-p2.xcor)**2+(self.ycor-p2.ycor)**2)**(1/2)
        return(dist)
        
point1=Point(3,5)
point2=Point(8,9)
print(point1.distance(point2))

 #problem_12
class Line(Point):
    def __init__(self,p1,p2):
        self.p1,self.p2=p1,p2
da_line=Line(point1,point2)
print(da_line)

        
        
        
    
            
            
       
        
