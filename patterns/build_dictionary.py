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
    
    def __getitem__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        # No key found, stop execution and throw an error 
        raise KeyError(f"Key {key} not found")
    
    # 1. get() - Return value or None if missing
    def get(self, key, default=None):
        try:
            return self[key] # Python automatically calls the function __getitem__(key) here 
        except KeyError:
            return default

    # 2. keys() - Return all keys (nested for loop, time complex: O2)
    def keys(self):
        return [k for bucket in self.table for k, v in bucket]

    # 3. values() - Return all values
    def values(self):
        return [v for bucket in self.table for k, v in bucket]

    # 4. items() - Return key-value pairs
    def items(self):
        return [(k, v) for bucket in self.table for k, v in bucket]

   
    ''' 
    5. pop(key) - Remove and return value of a given key. Since we know the index by using the hash key, 
    we do not need to search for entire table. We already know the bucket we have to search the key for.
    ''' 
    def pop(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i) # calls python built in list pop(i) method to pop the index 
                self.size -= 1
                return v
        raise KeyError(f"Key {key} not found")

    # 6. popitem() - Remove and return last item
    def popitem(self):
        for bucket in reversed(self.table):
            if bucket:
                k, v = bucket.pop()
                self.size -= 1
                return (k, v)
        raise KeyError("Dictionary is empty")


    # 7. clear() - Remove all items
    def clear(self):
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    # 8. copy() - Shallow copy
    def copy(self):
        new_dict = Dictionary(self.capacity)
        for k, v in self.items():
            new_dict[k] = v # calls new_dict.__setitem__(k)
        return new_dict

    # 9. setdefault() - Get value, set if missing
    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default 

    # 10. update() - Add/update from another dict. This function merge another dict into our current dict
    def update(self, dif_dict):
        for k, v in dif_dict.items():
            self[k] = v

    # 11. fromkeys() - Create a dictionary from given keys with same default value for all keys 
    # @classmethod lets us call the method on the class itself, 
    # by doing this we can hm = Dictionary.fromkeys(['a', 'b', 'c'], 0) instead of calling any instance of the class 
    @classmethod 
    def fromkeys(cls, keys, value=None):
        new_dict = cls()
        for key in keys:
            new_dict[key] = value
        return new_dict

    def __len__(self):
        return self.size 
    
    def __str__(self):
        return str(dict(self.items()))


'''
Simple test to verify if our custom dictionary works as intented  
'''
hobby = Dictionary()

# Add item to to out dictionary 
most_passionate = [5, 4, 3, 2, 1]
hobby_list = ["Football", "Cricket", "Drawing", "Music", "Coding"]
for i in range(len(most_passionate)):
    hobby[most_passionate[i]] = hobby_list[i]
print(hobby)

# 1. get(key) - Return value or None if missing
print(hobby.get(2))

# 2. keys() - Return all keys
print(hobby.keys())

# 3. values() - Return all values
print(hobby.values())

# 4. items() - Return key-value pairs
print(hobby.items())

# 5. pop(key) - Remove a key and return value of that key
print(f"Removed provded key, value of that key is: {hobby.pop(1)}")

# 6. popitem() - Remove and return last item
print(f"Removed last item, value of the last key is: {hobby.popitem()}")

# 8. copy() - Shallow copy
hobby_extended_one = hobby.copy()
hobby[6] = "Chess"
print(hobby_extended_one)

# 9. setdefault(key, value) - Get value, set if missing
print(hobby.setdefault(8)) # returns none since we do not have key of 8
print(hobby.setdefault(7, "Pool")) # pool, set key 7 = Pool
print(hobby)

# 10. update(dictionary) - Add/update from another dict
hobby_extended_two = hobby_extended_one.copy()
hobby_extended_two[9] = 'Swimming'
hobby.update(hobby_extended_two)
print(hobby)

# 11. fromkeys([list], default_value) - Create from keys with default value
person = Dictionary.fromkeys(["Name", "Age", "Address"], '')
print(person)

# 7. clear() - Remove all items
hobby.clear()
hobby_extended_one.clear()
hobby_extended_two.clear()
person.clear()

print(hobby)
print(hobby_extended_one)
print(hobby_extended_two)
print(person)


