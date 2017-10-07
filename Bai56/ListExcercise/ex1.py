def get_differ_between_list(list1, list2):
    # list_inter = []
    for i in list1:
        if i in list2:
            list1.remove(i)
            list2.remove(i)
    return list1 + list2
l1 = ['a','b','c']
l2 = ['a','d','1']
print get_differ_between_list(l1, l2)




