def change_str(str):
    if str[len(str)-3:] == "ing":
        return str + "ly"
    else :
        return  str + "ing"

print change_str("oanh")
print change_str("vaning")
print change_str("abc")
print change_str("string")
