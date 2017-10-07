def split_str(str):
    if len(str) == 1:
        return "Empty String"
    elif len(str) ==2 :
        return str*2
    else:
        return str[0:2] + str[len(str) - 2::]
print splitStr('w3resource')
print splitStr('w3')
print splitStr('w')
print splitStr('oanhpv')
