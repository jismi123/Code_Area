def makemytrip(string):
    n=len(string)
    if n%3!=0:
        return False
    segments=n//3
    for i in range(segments):
        if string[i]!=string[i+segments] or string[i]!=string[i+2*segments]:
            return False
    return True

string=input()
print(makemytrip(string))
