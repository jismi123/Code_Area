arr=list(input().split())
dictionary={}
for i in arr:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
max_value=0
max_char=None
for char,value in dictionary.items():
    if value>max_value:
        max_char=char 
        max_value=value 
print(max_char,max_value)
    
