class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for _ in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.Max
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()

t['march 9'] = 306
t["dec 30"] = 88
res = t['march 9']
print(res)
print(t.arr)