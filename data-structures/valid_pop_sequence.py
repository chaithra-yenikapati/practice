"""
pushSeq = [1, 2, 3]
popSeq = [3, 1, 2]

"""
def isValid(pushSeq, popSeq):
    buffer = []
    i = 0
    for val in popSeq:
        if buffer and val == buffer[-1]:
            buffer.pop()
            continue

        while((not buffer or buffer[-1] != val) and i < len(pushSeq)):
            buffer.append(pushSeq[i])
            i += 1

        if not buffer or buffer[-1] != val:
            return False
        buffer.pop()
    return True

print(isValid([1,2,3], [1, 2, 3]))
print(isValid([1,2,3], [1, 3, 2]))
print(isValid([1,2,3], [2, 1, 3]))
print(isValid([1,2,3], [2, 3, 1]))
print(isValid([1,2,3], [3, 1, 2]))
print(isValid([1,2,3], [3, 2, 1]))
print(isValid([1,2,3], [1, 2, 3, 4]))
print(isValid([1,2,3], [3, 2]))