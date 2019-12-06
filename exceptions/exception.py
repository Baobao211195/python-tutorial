"""
    + woring exception in python
    + except has contain many exception eg(except (RuntimeError, TypeError, NameError))
    + 
"""

def raise_exception():
    while True:
        try:
            x = int(input("please enter a number " ))
            break
        except NameError:
            print("ooop! please try again ")




def skip_exception(file): 
    """
    + # print error skip name of error on the last except
    """
    import sys
    try:
        f = open(file)
        s = f.readline()
        i = int(s.strip())
        print('value of i ', i)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except: 
        print("Unexpected error:", sys.exc_info()[0])
        raise



def try_else():
    """
    + use else when try does not raise exception
    
    """
    pass

if __name__ == "__main__":
    # raise_exception()
    # skip_exception('exception.txt')
    try_else()
    pass
