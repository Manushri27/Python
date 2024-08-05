s = input('enter a string :')
print (s[-1]+s[1:-1]+s[0]
       if len(s) > 1 
       else s
)