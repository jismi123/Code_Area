s=input()
c=input()
if c.isupper():
    s=s.replace(c,chr(ord(c)+32))
else:
    s=s.replace(c,chr(ord(c)-32))
print(s)
