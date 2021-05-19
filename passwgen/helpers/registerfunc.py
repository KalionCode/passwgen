registered = []
def main(n, mode=1):
    # mode 1 : register function

    def register_func_wrapper(func):
        try:
            registered[n] = func
        except IndexError as e:
            print(f'IndexError on registering function {func.__name__} at {n}')
    return register_func_wrapper

def registerfunc_init(n):
    global registered
    registered = [None for _ in range(n+1)]
    def passFunc(func):
        return func
    return passFunc

def registerfunc_getRegistered():
    return registered


    


