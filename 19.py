def insert(main,substr):
    mid = len(main)//2
    new_str = main[:mid] + substr + main[mid:]
    return new_str
mainstr = input("Enter your main string :")
substr = input("enter your sub string : ")

res = insert(mainstr,substr)
print(res)
