class a:
    def fff(self):
        super(a,self).hhh()


class b:
    def hhh(self):
        print('a')


class c(a, b):
   pass

c = c()
c.fff()

123
我是分支
123