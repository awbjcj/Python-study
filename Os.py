import os,time
# path = os.path.abspath('.')
# fileNum, fileSize, dirNum = 0, 0, 0

# for name in os.listdir(path):
#     if os.path.isfile(name):
#         print('%s\t\t%d \t%s'%(time.strftime('%Y/%m/ %H:%M',time.localtime(os.path.getmtime(name))),os.path.getsize(name),name))
#         fileNum += 1
#         fileSize += os.path.getsize(name)
#     if os.path.isdir(name):
#         print('%s\t\t<DIR>\t\%s'%(time.strftime('%Y/%m/ %H:%M',time.localtime(os.path.getmtime(name))),name))
#         dirNum += 1
# print('\t\t%d File(s)\t%d bytes'%(fileNum,fileSize))
# print('\t\t%d Dir(s)'%dirNum)

def search(text:str, path = '.') -> None:
    for name in os.listdir(path):
        nextPath = os.path.join(path, name)
        if os.path.isdir(nextPath):
            search(text, nextPath)
        elif name.find(text) != -1:
            print(nextPath)
            found = True
    

text = input('Please input the string to start searching files\n')
search(text)