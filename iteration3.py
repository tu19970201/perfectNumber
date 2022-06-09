maxNum = 100
candidate = 2
perfectNum = []
while candidate <= maxNum:
    i = 1
    sumF = 0
    while i < candidate:
        if candidate % i == 0:
            sumF += i
        i += 1
    if sumF == candidate:
        perfectNum.append(candidate)
    candidate += 1
print(maxNum , '以內的完美數有', perfectNum)