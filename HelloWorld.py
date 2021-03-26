n = int(input())

dict1 = {None : ['global']}
dict2 = {'global': []}
def add(namesp, arg):
    if len(arg) <= 10:
        if (str(namesp) in dict2.keys()):
            dict2[namesp].append(str(arg))
        else:
            dict2[str(namesp)] = str(arg)

def create(parent, namesp):
    if len(namesp) and len(parent)<=10:
        if (str(namesp)) in dict1.keys():
            dict1[namesp].append(str(parent))
        else:
            dict1[namesp]= [str(parent)]



def get(namesp, arg):
    parent = 0
    for i in dict2.keys():

        if i == namesp:
            parent = namesp
            for j in dict2[i]:
                if arg == j:
                    return parent

            for i in dict1.keys():
                for j in dict1[i]:
                    if j == parent:
                        parent = i
                        return get(parent, arg)



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