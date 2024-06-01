def check(x: str, file: str):
    list = x.lower().split(' ')
    list.sort()
    d = dict.fromkeys(list, 0)
    for st in list:
        d[st] += 1
    f = open(file, "w")
    for key in d:
        f.write(key + ' ' + str(d[key]) + '\n')
    f.close()