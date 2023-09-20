def validity(password):
    if len(password)<8:
        return False
    if not password[0].isupper():
        return False
    has_digit=False
    has_chara=False
    for i in password:
        if i.isdigit():
            has_digit=True
        elif i in "@$%&":
            has_chara=True
        if has_digit and has_chara:
            return True
    
password=input()
a= validity(password)
if a:
    print("True")
else:
    print("False")
