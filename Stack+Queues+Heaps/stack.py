class stack:
    s = []
    def push(self, a):
        self.s.append(a)

    def pop(self):
            if len(self.s) > 1:
                x = self.s[-1]
                del self.s[-1]
                return x
            elif (len(self.s) == 1):
                x = self.s[0]
                del self.s[0]
                return x
            else:
                print("Error, no elements")

    def len(self):
        return len(self.s)

s = stack()
print(s.len())
for i in range(2):
    s.push(int(input()))
for i in range(2):
    print(s.pop())
print(s.len())
