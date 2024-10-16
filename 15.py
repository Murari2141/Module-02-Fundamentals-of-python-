str1 = input("Enter a Word: ")
if len(str1) >= 3 :
    if str1.endswith("ing"):
        result = str1 + "ly"
    else :
        result = str1 + "ing"
else :
    print("length should be at least 3 ")
    
print(result)
