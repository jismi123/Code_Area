s = input()
c=1 
i=1 
while i< len(s):
    if s[i] == s[i - 1]:
       
        c += 1
    else:
        print(s[i - 1], end="")
        if c==1:
            print(end="")
        else:
            print(c, end="")
        c = 1
    i += 1
print(s[i - 1], end="")
print(c)
