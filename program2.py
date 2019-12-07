def upper(arg):
    if isinstance(arg, str):
        arg = arg.upper()
    return arg

def lower(arg):
    if isinstance(arg, str):
        arg = arg.lower()
    return arg

def replace(arg1, arg2, arg3):
    arg3=arg3.replace(arg1,arg2)
    return arg3

def join(arg1, arg2):
    return arg1+arg2

def len(arg):
    i=0
    for c in enumerate(arg):
        i=i+1
    return i
