class queue:
    q = []

    def lenq(self):
        return len(self.q)

    def enq(self, a):
        self.q.append(a)

    def deq(self):
        if self.lenq() >= 1:
            x = self.q[0]
            del self.q[0]
            return x
        else:
            print("No more elements")

q = queue()
print(q.lenq())
for i in range(2):
    q.enq(int(input()))

for i in range(2):
    print(q.deq())

print(q.lenq())
