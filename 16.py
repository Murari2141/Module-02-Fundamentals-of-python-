string = input("Enter Your String :").split()
big_len = 0

for i in string :
    if len(i) > big_len:
        big_len = len(i) 
      
print(big_len)     


