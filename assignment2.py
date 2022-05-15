#-----------QUESTION 1-------------------
print("-----------QUESTION 1-------------------")
str = "Python is a case sensitive language"
#----------Part a-------------------------
print("----------Part a-------------------------")
len = len(str)
print(len)
#----------Part b-------------------------
print("----------Part b-------------------------")
rev = str[::-1]
print(rev)
#----------Part c-------------------------
print("----------Part c-------------------------")
print(str[10:-9])
#----------Part d-------------------------
print("----------Part d-------------------------")
print(str.replace("a case sensitive","object oriented"))
#----------Part e-------------------------
print("----------Part e-------------------------")
print(str.index('a'))
#----------Part f-------------------------
print("----------Part f-------------------------")
print(str.replace(" ",""))

#-----------QUESTION 2-------------------
print("\n-----------QUESTION 2-------------------")
name = input("Enter your name: ")
sid = int(input("Enter Your SID: "))
department = input("Enter your department: ")
cg = float(input("Enter your CGPA: "))
pr = 'Hey, {} Here! \nMy SID is {}\nI am from {} department and my cg is {}'.format(name,sid,department,cg)
print(pr)

#-----------QUESTION 3-------------------
print("\n-----------QUESTION 3-------------------")
a = 56
b = 10
print("----------Part a-------------------------")
print(a & b)
#----------Part b-------------------------
print("----------Part b-------------------------")
print(a | b)
#----------Part c-------------------------
print("----------Part c-------------------------")
print(a ^ b)
#----------Part d-------------------------
print("----------Part d-------------------------")
print(a<<2 , b<<2)
#----------Part e-------------------------
print("----------Part e-------------------------")
print(a>>2 , b>>4)

#-----------QUESTION 4-------------------
print("\n-----------QUESTION 4-------------------")
string = input("Enter the string: ")
if 'name' in string:
    print("YES")
else:
    print("NO")

#-----------QUESTION 5-------------------
print("\n-----------QUESTION 5-------------------")
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
d = a + b <= c or a + c <= b or c + b <= a
match d:
    case True:
        print("YES")
    case False:
        print("NO")

#-----------QUESTION 6-------------------
print("\n-----------QUESTION 6-------------------")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = bin(a^b)     
d = c.count('1')
print(d)
