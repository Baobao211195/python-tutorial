def remove_duplicate(str):
    list = str.split(",")
    return sorted(set(list))

print remove_duplicate("red, white, black, red, green, black")