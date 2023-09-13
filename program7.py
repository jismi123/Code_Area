def moveHash(s):
    x=s.count("#")
    s=s.replace("#","")
    return "#"*x+s 
    
s=input()
print(moveHash(s))
