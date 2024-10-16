num = int(input("Enter Your Number: "))
factorial = 1

if num > 0:
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)
else:
    print("please enter valid number.")
    
    
    
