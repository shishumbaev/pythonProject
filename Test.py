dict1 = {'None': ['global'], 'global': ['first'], 'first': ['second'], 'second': ['third']}
dict2 = {'global': [], 'first': ['my_var'], 'second': [], 'third': []}



def get(namesp, arg, z=dict2):
    s = 0
    d = 0
    for i, j in z.items():
        if j == [] and i == namesp:
            d = i
        else:
            for j in z[i]:
                if arg == namesp:
                    return namesp
                if namesp == i:
                    d = i
                if arg == j:
                    s = i
                    if namesp == i:
                        return s

        if s != 0 and d != 0:
            return get(s, rec(s, d), z=dict1)

def rec(s, d):
    for i in dict1.keys():
        for j in dict1[i]:
            if s == d:
                return d
            if d == j:
                d = i
            if d == i:
                return rec(s,d)







print(get('third', 'my_var'))
print(get('foo', 'c'))
print(get('bar', 'a'))
print(get('bar', 'b'))










#n, k = map(int, input().split())
#def rec(n,k):
#    if k == 0:
#        return 1
#    elif k>n:
#        return 0
#    else:
#        return rec(n-1, k) + rec(n-1, k - 1)
#y = rec(n,k)
#print(y)
