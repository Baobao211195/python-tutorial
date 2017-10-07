def count_word(str):
    dic = {}
    for i in str.split(" "):
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return  dic


print count_word("oa oa van oanh pa pa")


