a=int(input("Enter length of first side : "))
b=int(input("Enter length of second side : "))
c=int(input("Enter the length of third side :"))
s=0
s=float(a+b+c)/2 #formula for calculate semiparameter
area=float(s*(s-a)*(s-b)*(s-c))**0.5   #formula for area of triangular
print("the area of Triangular is: ",area)
