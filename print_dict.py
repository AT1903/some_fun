import pprint
d = {'key1':{'k11':['v11','v112'],'k12': 'v12','k13':'v13'},'key2':{'k21':'v21','k22': 'v22','k23':'v23'}}
print(d)


def print_d(d, indent=0):
    s = "______"
    for key, value in d.items():
        print(s * indent + str(key))
        if isinstance(value, dict): # вернет True, если проверяемый объект object является экземпляром словаря
            print_d(value, indent+1)
        else:
            print(s * (indent+1) + str(value))

print_d(d)