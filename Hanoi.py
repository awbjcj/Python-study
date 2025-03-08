def move(n:int, a:str, b:str, c:str)->None:
    '''intro of the func'''
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(5, 'A', 'B', 'C')