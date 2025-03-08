from functools import reduce
def str2float(s):
    decimal_pos = s.find('.')
    s_int, s_float = s.split('.')
    return reduce(lambda x,y:10*x+y, map(char2digit, s_int)) + reduce(lambda x,y:10*x+y, map(char2digit, s_float))/pow(10, len(s_float))
    
def char2digit(c):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dict[c]

print('str2float(\'123.45678\') =', str2float('123.45678'))
if abs(str2float('123.45678') - 123.45678) < 0.000001:
    print('测试成功!')
else:
    print('测试失败!')

