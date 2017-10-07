def change_str(str):
    char = str[0]
    print char
    str1 = str.replace(char, "$")
    print str1
    str1 = char + str1[1:]
    print str1
    return  str1

print change_str("restart")