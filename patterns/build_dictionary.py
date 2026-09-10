'''
In this example we will create a custom dictionary data structure with all major methods that are avaiable in python.
By practicing how to build dictionary ds, you will be avail to understand how it works under the hood. One other reason
to learn how to build dictionary is that it is a common interview question. After building our own data structure we will 
attempt to solve some question using it. 
'''

class Dictionary:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    # _ means private, in python modulo with a positive divisor always returns positive result even if first number is negative 
    def _hash(self, key):
        return hash(key) % self.capacity # hash() is python built in function that converts any object into an integer 

    # This is a special method, when we call dictionary dn['a'] = 1 python auto will call this dn.__setitem__['a'] = 1
    def __setitem__(self, key, value):
        # add or update key:value 
        index = self._hash(key)
        bucket = self.table[index]

        # check if the key already exists 
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key does not exists, therefore we add a new one 
        bucket.append((key, value))
        self.size += 1

dn = Dictionary()
print(dn.capacity)
print(dn.table)
print(dn.size)
print(dn._hash("Yes"))