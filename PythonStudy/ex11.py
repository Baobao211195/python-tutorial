# -*- coding: utf-8 -*-
# bài này là liên quan đến nhập dữ liệu từ bàn phím
# sử dụng hàm input() trong python 3
# trong python 2. bản thấp hơn thì dùng hàm raw_input
print("Ban bao nhieu tuoi")
age = int(input("tuoi cua ban la : ")) # kiểu giá trị trả về của age là kiểu string.
# ta phải đổi về kiểu số tự nhiêu....vì đây là nhập tuổi 
print(type(age))
#print("Tuoi cua ban la %d " %age)
print(" chieu cao cua ban la bao nhie ?")
height = input("chieu cao:")
print(" can nang cua ban la bao nhieu?")
weight = input("can nang :")
