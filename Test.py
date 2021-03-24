dict1 = {'None': ['global'], 'global': ['foo'], 'foo': ['bar'], 'bar': ['zoo'], 'barz': ['bary'], 'zoo': ['doo'], 'zoo2': ['zoo3']}
dict2 = {'global': [], 'foo': [], 'barz': ['b'], 'bary': ['b'], 'bar': ['b'], 'zoo': [], 'zoo2': [], 'zoo3': [], 'doo': []}



def get(namesp, arg, z=dict2):
    s = 0
    d = 0
    for i in z.keys():
        if i == namesp:
            d = i
            if s != 0 and d != 0:
                if rec(s, d) != None:
                    return rec(s, d)
        else:
            for i in z.keys():
                if namesp == i:
                    d = i
                for j in z[i]:
                    if i == j:
                        return namesp
                    if arg == j:
                        s = i
                        if s != 0 and d != 0:
                            if rec(s,d) != None:
                                return rec(s,d)




def rec(d, s):
    for i, j in dict1.items():
        for j in dict1[i]:
            if i == d and s == j:
                return d
            if i == s and j == d:
                return s
            if s == d:
                return d
            if s == 'global':
                return rec(s,d)
            if d == j:
                if s == i:
                    d = i
                    return rec(d,s)



print(get('zoo', 'b'))








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
