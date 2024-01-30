#PYthon program to find the FACTORIAL of a NUMBER
#To understand this example, you should have the knowledge of the following
#i)Python if...else Statement
#ii)Python for Loop
#iii)Python Recursion

#1.TO FIND THE FACTORIAL OF A NUMBER USING LOOP without taking user input

number=6
factorial=1

if number<0:
    print('Sorry, factorial does not exist for negative numbers')
elif number==0:
    print('The factorial of 0 is 1')
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print('The factorial of',number,'is',factorial)
    


#2.FACTORIAL OF A NUMBER USING RECUSRION

# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    '''This is a recursive function
       to find the the factorial of an integer'''
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
    
num=7
result=factorial(num)
print('The factorial of',num,'is',result)
    



    
