#HashSet -It is a set based data structure which stores values
#Similar to List or a set time but fast and constant which is O(1) - which is constant that means it will
#takes 1 min to retreive 1 record accordingly it will take 2 min to retrive 2 records and so on.
#Hashing is used to search for values in hashet       [2,7][3]
#For example :- we define a hash table Hash =     [N,N,N,N,N] Hash Table size = 5
#                                                  0 1 2 3 4
#For adding,removing and searching we will calculate hash value i.e the position at which value will be added.
#we will calcualte hash value[hv] of 2 HV = Value which you want to add in hash table * Size of Hash table = 2 % 5 = 2
#so add 2 on 2nd Index hv = 3 % 5 = 3, hv = 7 % 5 = 2 - In this case we will append 7 on 2nd index [2,7]

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.calculate_hash_value(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            return key in self.table[hv]
        return False


# Your MyHashSet object will be instantiated and called as such:
#obj = MyHashSet()
#obj.add(1)
#obj.add(2)
#obj.contains(1) - True
#obj.contains(3) - False
#obj.add(2)
#obj.contains(2) - True
#obj.remove(2)
#obj.contains(2) - False
#print(obj.table)
# obj.remove(key)
# param_3 = obj.contains(key)

