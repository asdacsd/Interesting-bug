class a:
    def fff(self):
        super(a,self).hhh()

这是tt的提交
class b:
    def hhh(self):
        print('a')


class c(a, b):
   pass

c = c()
c.fff()
