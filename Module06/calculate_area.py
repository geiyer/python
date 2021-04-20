def area(l, w):
    if (l <0 or w< 0):
        raise ValueError("Only positive integers, please")

    return l*w