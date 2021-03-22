n = int(input())

dict1 = {'None':['global']}
dict2 = {'global': []}
def add(namesp, arg):
    if len(arg) <= 10:
        if (str(namesp) in dict2.keys()):
            dict2[namesp].append(str(arg))
        else:
            dict2[str(namesp)] = str(arg)

def create(parent, namesp):
    if len(namesp) and len(parent)<=10:
        dict1[str(namesp)] = [str(parent)]
        dict2[str(parent)] = []


def get(namesp, arg, z=dict2):
    s = 0
    d = 0
    for i, j in z.items():
        if j == [] and i == namesp:
            d = i

        else:
            for i in z.keys():
                for j in z[i]:
                    if i == j:
                        return namesp
                    if namesp == i:
                        d = i
                        if arg == j:
                            s = i
                            if namesp == i:
                                return s
                    if arg == j:
                        s = i
                    if s != 0 and d != 0:

                        return rec(s, d)


def rec(s, d):
    for i, j in dict1.items():
        for j in dict1[i]:
            if i == s and d == j:
                return s
            if s == d:
                return d
            if d == j:
                d = i
                return rec(s,d)



if 1<= n <= 100:
    for i in range(n):
        cmd, namesp, arg = input().split()
        if cmd == 'add':
            add(namesp, arg)
        elif cmd == 'create':
            create(namesp, arg)
        elif cmd == 'get':
            print(get(namesp, arg))


print(dict1)
print(dict2)