registered = []
def main(n):
    def register_func_wrapper(func):
        global registered
        if (n > len(registered)-1 ):
            for _ in range(n-(len(registered)-1)): registered.append(None)
        registered[n] = func

            
    return register_func_wrapper



def getRegistered():
    return registered


    


