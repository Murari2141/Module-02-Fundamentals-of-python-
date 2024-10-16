n = int(input("enter Fibonacci series range value : "))
a = int(input("enter first Fibonacci series 1st value : "))
b = int(input("enter first Fibonacci series 2nd value : "))

print(a , b , end=" ")

for i in range (3,n+1):
    c = a + b
    a = b
    b = c
    print(c , end = " ")
