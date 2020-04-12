sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}, 'hobbies':['Music', 'Running']}
print('Original File: ', sample_object)


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

print('Converted File: ', flatten_json(sample_object))

### Output ###
#Original File:  {'Name': 'John', 'Location': {'City': 'Los Angeles', 'State': 'CA'}, 'hobbies': ['Music', 'Running']}
#Converted File: {'Name': 'John', 'Location_City': 'Los Angeles', 'Location_State': 'CA', 'hobbies_0': 'Music', 'hobbies_1': 'Running'}
