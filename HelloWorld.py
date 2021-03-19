n = int(input())

dict1 = {'None':'global'}
dict2 = {'global': []}
def add(namesp, arg):
    if str(namesp) in dict2.keys():
        dict2[namesp].append(str(arg))
    else:
        dict2[str(namesp)] = str(arg)

def create(parent, namesp):

    dict1[str(namesp)] = [str(parent)]
    dict2[str(parent)] = []

s
def get(namesp, arg, z=dict2):

    s = 0
    d = 0
    for i in z.keys():
        for j in z[i]:
            if arg == namesp:
                return namesp
            if namesp == i:
                d = i
            if arg == j:
                s = i
                if namesp == i:
                    return s

            if s !=0 and d !=0:
                return get(s, rec(s,d), z=dict1)

def rec(s, d):
    for i in dict1.keys():
        for j in dict1[i]:
            if s == d:
                return d
            if d == j:
                d = i
            if d == i:
                return rec(s,d)




for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
    else:
        print(get(namesp, arg))

print(dict1)
print(dict2)