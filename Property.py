class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value <= 0:
           raise ValueError("Invalid width!")
        else:
           self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value <= 0:
           raise ValueError("Invalid height!")
        else:
           self._height = value
    
    @property
    def resolution(self):
        return self.width * self.height
        
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')