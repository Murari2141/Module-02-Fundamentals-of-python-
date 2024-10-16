def revstr(string):
    if len(string) % 4 == 0:
        return string[::-1]
    

string1 = input("enter a string:")   
res = revstr(string1) 

print(res)