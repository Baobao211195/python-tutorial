str = "google.com"
dics ={}
for i in str:
    if i in dics.keys():
        dics[i] += 1
    else:
        dics[i] = 1
print dics
