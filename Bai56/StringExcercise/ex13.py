# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# def merge_list(original_list):
#     str1 = []
#     for i in original_list:
#         for z in i:
#             str1.append(z)
#     return str1
#
# print merge_list(original_list)
def merge_list_2(list1):
    str1 = " "
    for i in list1:
        str1 += ' '.join(map(str,i)) + " "
    return map(int,str1.strip().split(' '))

print merge_list_2([[2,4,3],[1,5,6], [9], [7,9,0]])