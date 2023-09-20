num=input()
new=num[::-1]

sum1=int(new[0])+int(new[1])
print(sum1)
if sum1==3 or sum1==8:
    print("Lucky Draw Winner")
else:
    print("Not a lucky draw winner")
