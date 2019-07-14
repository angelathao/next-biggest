def next_bigger(n):
    """This takes a positive integer number and returns the next bigger number formed by the same digits"""
    from itertools import permutations

    numlist = [int(i) for i in str(n)]
    perm = list(permutations(numlist, len(numlist)))
    concat_numlist = [int("".join([str(i) for i in j])) for j in perm]
    concat_numlist.sort()

    if concat_numlist.index(n) == len(concat_numlist) -1:
        return -1
    else:
        return concat_numlist[concat_numlist.index(n) + 1]



print(next_bigger(510))
print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(9))