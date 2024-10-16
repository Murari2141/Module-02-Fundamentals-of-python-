str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str2[:2] + str1[2:]
str2 = str1[:2] + str2[2 :]

print(str1+" "+str2)


