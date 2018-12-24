def sample():
    n = 0
    # Closure function
def func():
    print('n=', n)

    # Accessor methods for n
def get_n():
    return n

def set_n(value):
    global n
    n = value

    # Attach as function attributes
func.get_n = get_n
func.set_n = set_n
return func

