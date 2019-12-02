"""
+ File in python
"""
def read_file(file):
    """
    + read file in python
    'r' : only read
    'w' : only write
    'a' : open for appending (add to the end of file)
    'r+' : read and write
    mode is optional if is 'r' mode can be skiped
    if open file is not text should be add 'b' (binary mode)
    """
    f = open(file, 'r')
    print(f.read())
read_file('demo.txt')

def read_file_with_keyword(file):
    """
    + working to with keyword to processing file objects
    => file will close when occurs exception
    familiar to use try-finally
    """
    with open(file) as f:
        data = f.read()
        print(data)

    with open(file) as f2:
        data = f2.readlines()
        print(data)

read_file_with_keyword('demo.txt')

"""
+ some method of file object
+ read => return data as string
+ readLine() => read a single line (use loop to read all file )
+ readLines() => return a list of lines of file
"""

def write_file(file):
    pass
    
def working_json():
    """
    + Working json

    """
    import json
    return json.dumps([1,"oanh", 2323])

print("working json", working_json())