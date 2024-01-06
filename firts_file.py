


#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))








a = 0; b = 1
for _ in range(int(input())):
    print(a,end = " ")
    a+=b
    b = a- b




import textwrap

def wrap(string, max_width):
    first = 0
    mid = max_width
    last = mid+max_width
    old  = string[first:mid]+"\n"+string[mid:last]
    while(last <= len(string)):
        first = last
        mid = first+max_width
        last = mid+max_width
        old = old+"\n"+string[first:mid]+"\n"+string[mid:last]
    return old

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

prime= []
for i in range(2,1000):
    if all(i%io != 0 for io in range(2,i)):
        prime.append(i)    
print(prime)




n= int(input())
N= n
def summey(n,k):
    if n%k == 0:
        return int(((((n-k)//k)+1)*(k+(n//k)*k)/2)-n)
    else:
        return int(((((n-k)//k)+1)*(k+(n//k)*k)/2))
print(1,summey(n,3)+summey(n,5)-summey(n,15))
print(summey(n,3),((int((n-1)/3)+1)/2)*(int((n-1)/3)*3),(((N // 3)) * (2 * 3 + (N //3 - 1) * 3) //2))
print(summey(n,5),((int((n-1)/5)+1)/2)*(int((n-1)/5)*5),(((N // 5)) * (2 * 5 + (N //5 - 1) * 3) //2))
print(summey(n,15),((int((n-1)/15)+1)/2)*(int((n-1)/15)*15),(((N // 15)) * (2 * 15 + (N //15 - 1) * 15) //2))
print((((N // 3)) * (2 * 3 + (N //3 - 1) * 3) //2)+(((N // 5)) * (2 * 5 + (N //5 - 1) * 5) //2)-(((N // 15)) * (2 * 15 + (N //15 - 1) * 15) //2)-N)
print(int(((int((n-1)/3)+1)/2)*(int((n-1)/3)*3)+((int((n-1)/5)+1)/2)*(int((n-1)/5)*5)-((int((n-1)/15)+1)/2)*(int((n-1)/15)*15)))
for _ in range(int(input())):
    n = int(input().strip())
    p= ((n-3)*n/(2*3))+((n-5)*n/(2*5))-((n-15)*n/(2*15))
    print((int((n-1)/3)*(int((n-1)/3)+1)*3/2),(int((n-1)/5)*(int((n-1)/5)+1)*5/2),(int((n-1)/15)*(int((n-1)/15)+1)*15/2),int(p))


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            s += i
    print(s)












def word_merger(a,b):
    added = ""
    print(len(min(a,b)),len(a),len(b))
    for i in range(min(len(a),len(b))):
        added += a[i]+b[i]
    return added
print(word_merger("13579 11 13 15", "2468 10 12"))













if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(sum(scores)/len(scores),student_marks)



if __name__ == '__main__':
    m= []
    val = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        val.append(score)
        m.append([name,score])
    for i in list(set(sorted(val, reverse = True)))[1:2]:
        for j in sorted(m):
            if i == j[1]:
                print(j[0])
print(list(set(sorted(val,reverse = True))),list(set(sorted(val)))[1:2],sorted(m))




o=  map(int, input().split(" "))
k= set(o)
print(sorted(k,reverse = True))
print(sorted(k)[1])

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li = []
    for i in range(x+1):
        for u in range(y+1):
            for t in range(z+1):
                if i+u+t != n:
                    li.append([i,u,t])
                    
    print(li)



class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        c= 1
        self.maximumDifference = 0
        for i in self.__elements:
            for o in range(c,len(self.__elements)):
                if self.maximumDifference < diff(i,self.__elements[o]):
                    self.maximumDifference= diff(i,self.__elements[o])
            c += 1         
        
def diff(a,b):
    if a > b:
        return a-b
    else:
        return b-a

# End of Difference class by m1 

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


def diff(a,b):
    if a > b:
        return a-b
    else:
        return b-a
a = [int(e) for e in input().split(" ")]
print(a)
c= 1
dio = []
for i in a:
    
    for o in range(c,len(a)):
        dio.append(diff(i,a[o]))
    c += 1
print(dio)
print(max(dio))

print("\n")
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores = scores 

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(self.scores)/len(self.scores)
        if 90 <= average <= 100:
            return ("O")
        elif 80 <= average < 90:
            return("E")
        elif 70 <= average < 80:
            return("A")
        elif 55 <= average < 70:
            return("P")
        elif 40 <= average < 55:
            return("D")
        elif average < 40:
            return ("T")
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())



arr=[]
for _ in range(6):
    arr.append(list(map(int,input().rstrip().split())))
for ar in arr:
    print(ar)
sm = []
for u in range(4):
    for ui in range(4):
        sm.append(arr[ui][u]+arr[ui][u+1]+arr[ui][u+2]+arr[ui+1][u+1]+arr[ui+2][u]+arr[ui+2][u+1]+arr[ui+2][u+2])
print(sm)
print(max(sm))

a = int(input())
store = ""
while a != 0:
    store = str(a%2)+store
    a = a//2
print(len(max(store.split("0"))))

##
##
##
##
##
##print("Hello")
##a = 1110111011111
##print(len(max(str(a).split("0"))))
##import sys
##di = {}
##for i in range(int(input())):
##    print(i)
##    a=input().split(" ")
##    di[a[0]] = a[1]
#### way-1 multiple inputs end by ctrl+d
##try:
##    while True:
##        a=input()
##        if a in di:
##            print(f"{a}={di[a]}")
##        else:
##            print("Not found")
##except:
##    pass
#### for multiple inputs way-2
##lines = sys.stdin.readlines()
##for i in lines:
##    print(i,lines)
##    name = i.strip()
##    print(name)
##    if name in di:
##        print(name + '=' + str( di[name] ))
##    else:
##        print('Not found')
