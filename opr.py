def isint(string, stack):
    try:
        return int(string)
    except:
        return int(stack.get(string))


def teq(com1, com2, stack):
    c1 = isint(com1, stack)
    c2 = isint(com2, stack)
    if c1 == c2:
        return 1
    else:
        return 2

def tgt(com1, com2, stack):
    c1 = isint(com1, stack)
    c2 = isint(com2, stack)
    if c1 > c2:
        return 1
    else:
        return 2

def tlt(com1, com2, stack):
    c1 = isint(com1, stack)
    c2 = isint(com2, stack)
    if c1 < c2:
        return 1
    else:
        return 2

def tcp(com1, com2, stack):
    c1 = isint(com1, stack)
    c2 = isint(com2, stack)
    if c1 > c2:
        return 1
    elif c1 == c2:
        return 3
    else:
        return 2