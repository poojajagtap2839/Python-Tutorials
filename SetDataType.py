# Set returns the unique elements and its unordered collection hence cant access elemnets using index
# Sets are unchangable and enclosed by '{}'

mySet2= { }
print(type(mySet2))

mySet3=set()
print(type(mySet3))

mySet={'Red','Black','White','Yellow'}
for colour in mySet:
    print(colour)



s1={1,2,3,4}
s2={3,4,5,6,7,8}
print(s1.union(s2))                                        # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2))                                 # {3, 4}
print(s1,s2)                                               # {1, 2, 3, 4} {3, 4, 5, 6, 7, 8}
print(s1.symmetric_difference(s2))                         # {1, 2, 5, 6, 7, 8}


s1={2,3,4}
s2={5,6,7}
print(s1.isdisjoint(s2))                                   # True
print(s1.issuperset(s2))                                   # False
print(s1.issubset(s2))                                     # False


