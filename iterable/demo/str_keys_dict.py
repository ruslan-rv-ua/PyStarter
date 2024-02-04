class StringKeysIterator:
    def __init__(self, input_dict):
        self.keys = list(input_dict)
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.keys):
            key = self.keys[self.index]
            self.index += 1
            if isinstance(key, str):
                return key
        raise StopIteration

'''
class StringKeysIterator:
    def __init__(self, input_dict):
        self.keys = []
        for key in input_dict.keys():
            if isinstance(key, str):
                self.keys.append(key)
        
    def __getitem__(self, index):
        return self.keys[index]
'''

d = {
    1: 'один', 'один': 1,
    2: 'два', 'два': 2,
    3: 'три', 'три': 3,
    4: 'чотири', 'чотири': 4,
    5: 'п\'ять', 'п\'ять': 5,
}

#for str_key in StringKeysIterator(d):
#    print(str_key)
    
keys = StringKeysIterator(d)
keys_list = list(keys)

kl = list(StringKeysIterator({}))


from collections import UserDict
class MyDict(UserDict):
    def str_keys(self):
        return StringKeysIterator(self)
        
c = MyDict({
    1: 'один', 'один': 1,
    2: 'два', 'два': 2,
    3: 'три', 'три': 3,
    4: 'чотири', 'чотири': 4,
    5: 'п\'ять', 'п\'ять': 5,
})

for key in c.str_keys():
    print(key)


