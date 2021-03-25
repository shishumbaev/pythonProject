dict1 = {'None': ['global'], 'global': ['foo'], 'foo': ['bar'], 'bar': ['zoo'], 'barz': ['bary'], 'zoo': ['doo'], 'zoo2': ['zoo3']}
dict2 = {'global': [], 'foo': [], 'bary': ['b'], 'barz': ['b'], 'bar': ['b'], 'zoo': [], 'zoo2': ['b'], 'zoo3': [], 'doo': []}



def get(namesp, arg):
    list = []
    for i in dict2.keys():
        for j in dict2[i]:
            if arg == j:
                list.append(i)

    for i in dict2.keys():
        for j in dict2[i]:
            if j == arg:
                if i == namesp:
                    return namesp
                else:
                    for i in dict1.keys():
                        for j in dict1[i]:
                            if j == namesp:
                                namesp = i
                                return get(namesp, arg)







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
