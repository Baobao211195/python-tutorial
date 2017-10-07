# def add_tag(ch, str):
#     return "<%s>%s</%s>" %(ch,str,ch)

# print add_tag("i","oa")
# def fileter_list(lists):
#     count1 = 0
#     count2 = 0
#     for i in lists:
#         if len(i) == 2:
#            count1 += 1
#         if i[0] == i[-1]:
#             count2 += 1
#     print count1
#     print count2
# fileter_list(['abc', 'xyz', 'aba', '1221'])
# def remove_duplicate(lists):
#     return list(set(lists))

# print remove_duplicate(["oa","oa","ba"])
def find_word(n,lists):
    list_word = []
    for i in lists:
        if len(i) == 4:
            list_word.append(i)
    return list_word

# print find_word(4,['abc', 'xyz', 'aba', '1221'])
#
def find_element_common(list1, list2):
    for i in list1:
        if i in list2:
            return  True
        else:
            return False
# print find_element_common(['abc', 'xyz', 'aba', '1221'],['abc',1221])
def compare_list(l1,l2):
    return l1 == l2
# print compare_list(['a','bg'],['a'])

def random_list(l1):
    import random as rad
    return rad.choice(l1)
# print random_list([1,'a','4','bc'])

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print map(str,list2)
print map(slice,list2)
print type(' '.join(map(str, list2)))

# print('Compare list1 and list2')
# print type(map(set(),list1))
# print type(' '.join(map(str, list1*2)))
#
#

print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))





