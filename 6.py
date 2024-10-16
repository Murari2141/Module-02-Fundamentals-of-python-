num1 = input("enter number : ")
num2 = input("enter number : ")

temp = num1
num1 = num2
num2 = temp

print("num1 :",num1 , "num2 :",num2)

num1 , num2 = num2 , num1
print("swaping without temp varible : num1 :" , num1 , "num2 :",num2)