def findMinAndMax(L):
    if L is None or len(L) == 0:
        return (None, None)
    else:
        curr_min = L[0]
        curr_max = L[0]
        for curr_num in L:
            if curr_num > curr_max:
                curr_max = curr_num
            elif curr_num < curr_min:
                curr_min = curr_num
        return (curr_min, curr_max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')