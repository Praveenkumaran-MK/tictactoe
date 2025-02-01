f = [' ', '|', ' ', '|', ' ']
s = [' ', '|', ' ', '|', ' ']
t = [' ', '|', ' ', '|', ' ']


for i in range(1, 10, 1):
    class px:
        def _init_(self, xr, xc):
            self.xr = xr
            self.xc = xc
            if i % 2 == 0:
                self.x = 'x'
            else:
                self.x = 'o'
           

        def display(self):
            if self.xr == 'f':
                if self.xc == 0:
                    f[0] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                elif self.xc == 1:
                    f[2] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                else:
                    f[4] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
            elif self.xr == 's':
                if self.xc == 0:
                    s[0] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                elif self.xc == 1:
                    s[2] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                else:
                    s[4] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
            else:
                if self.xc == 0:
                    t[0] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                elif self.xc == 1:
                    t[2] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')
                else:
                    t[4] = self.x
                    print(f, '\n')
                    print(s, '\n')
                    print(t, '\n')

    print("welcome to turn ", i)
    xr = input("Enter row you need to mark (f, s, t): ")
    xc = int(input("Enter column you need to mark (0, 1, 2): "))
    p = px(xr, xc)
    p.display()

