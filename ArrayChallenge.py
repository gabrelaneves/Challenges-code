def ArrayFunction(arr):
    arr = [int(x) for x in arr]
    num_unique = list(set(arr))
    comb = list(itertools.combinations(num_unique, 2))
    double = sum(arr) * 2
    w = 0
    for x in comb:
        i, h = x
        if i * h >= double:
            w += 1
    if w >= 1:
        print("true")
    else:
        print("false")
    # code gos
    print(arr)


print(ArrayFunction(input()))

# return true
# if any 2 numbers can be multipleid so that
# the answers is greater that the double of the sum of
# all elements on the Array
