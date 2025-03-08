def trim(s):
    if s == '':
        return ''
    init_pos = 0
    while s[init_pos] == ' ' and init_pos < len(s)-1:
        init_pos += 1
    end_pos = -1
    while s[end_pos] == ' ' and end_pos > -len(s):
         end_pos -= 1
    if init_pos > len(s) + end_pos:
        return ''
    else:
        return s[init_pos:(len(s) + end_pos + 1)]
    
# 测试:
if trim('hello  ') != 'hello':
    print(trim('hello  '))
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')