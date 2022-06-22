#variable should not start with numeric andspace is not allowed in variable
# a=10  allowed
# a b=10  not allowed
# a_b=10 allowed
# 3a=10  not allowed
# a3=10   allowed

#Datatypes
#  int,float,char,string 
#  here no need to declare datatype,python understand

# we can write string in "" and '' qoutes both

print("Welcome to Python Programming")
print('i am js1 file')
 
 #addition

a = 10
print('value of a is: ',a)
b = 20
print('value of b is: ',b)
sum=a+b
print("sum is: ",sum)

#subtraction
a = 10
print('value of a is: ',a)
b = 20
print('value of b is: ',b)
sub=b-a
print("subtraction is: ",sub)


#multiplication
a = 10
print('value of a is: ',a)
b = 20
print('value of b is: ',b)
mul=a*b
print("multiplication is: ",mul)


#division
a = 10
print('value of a is: ',a)
b = 20
print('value of b is: ',b)
div=b/a
print("division is: ",div)

#user input

a=input("enter the value of a:")
print('value of a is: ',a)
b=input("enter the value of b:")
print('value of b is: ',b)
sum=a+b  #here it will consider input as string so we need to type cast to int
print("sum is: ",sum)

a=int(input("enter the value of a:"))
print('value of a is: ',a)
b=int(input("enter the value of b:"))
print('value of b is: ',b)
sum=a+b  
print("sum is: ",sum)
