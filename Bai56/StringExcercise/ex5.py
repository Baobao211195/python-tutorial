def change_str(str):
    if str.rfind("not") <= 0  & str.rfind("poor") <= 0:
        return str.replace(str[str.rfind("not"):str.rfind('poor')+len("poor")],"good")
    else:
        return str


print change_str("oanh not that poor ha nam")
print change_str("oanh not that  ha nam")
