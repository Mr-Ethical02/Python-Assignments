'''
Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number. For instance:[2, 4, 10, 20, 5, 2, 20, 4]
'''
l = [2, 4, 10, 20, 5, 2, 20, 4]
def remdup(l):
    l = set(l)
    l = list(l)
    return l
print("\nList before removing duplicates:",l)
print("\nList after removing duplicates:",remdup(l))