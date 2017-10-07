def get_length_element_list(lists):
    list_length = []
    for i in lists:
        list_length.append(len(i))
    return  max(list_length)
#

print get_length_element_list(['oa321',"va","tradfadfeae"])