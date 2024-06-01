def find_modified_max_argmax(L, f):
    L = [f(i) for i in L if type(i) is int]
    return (a := max(L), L.index(a)) if L else ()