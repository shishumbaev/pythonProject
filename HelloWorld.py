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


def get(namesp, arg):
    for i in dict2.keys():
        for j in dict2[i]:
            if i == namesp:
                if j == arg:
                    return namesp
                else:
                    for i in dict1.keys():
                        for j in dict1[i]:
                            if j == namesp:
                                namesp = i

                                return get(namesp, arg)















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