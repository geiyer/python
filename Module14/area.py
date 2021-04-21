def calculate_area(l, w):
    if (isinstance(l, str) or isinstance(w, str)):
        raise ValueError

    if l < 0 or w < 0:
        raise ValueError

    return l* w