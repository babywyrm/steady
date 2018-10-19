def fibFastRec(n):
    def fib(prvprv, prv, c):
        if c < 1: return prvprv
        else: return fib(prv, prvprv + prv, c - 1)
    return fib(0, 1, n)

for i in range(1,31):
    print(fibFastRec(i))