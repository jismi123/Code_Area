def longest(st):
    words=st.split()
    max_length=-1
    max_leng_word=""
    for i in words:
        length=len(i)
        if length%2==1 and length>max_length:
            max_length=length
            max_leng_word=i 
    print(max_leng_word)
x=int(input())
st=input()
longest(st)
