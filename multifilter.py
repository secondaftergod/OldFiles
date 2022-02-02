class multifilter:

    def judge_half(self, par, pos=0, neg=0):
        for j in self.funcs:
            if j(par) == True:
                pos += 1
            else:
                neg += 1
        if pos >= neg:
            return True

    # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
# ----------------------------------------
    def judge_any(self, par, pos=0, neg=0):
        for j in self.funcs:
            if j(par)==True:
                pos+=1
            else:
                neg+=1
        if pos>=1:
            return True
    # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
# ----------------------------------------
    def judge_all(self, par, pos=0, neg=0):
        for j in self.funcs:
            if j(par) == True:
                pos += 1
            else:
                neg += 1
        if neg==0:
            return True
    # допускает элемент, если его допускают все функции (neg == 0)
#----------------------------------------
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            if self.judge(self, i)==True:
                yield i
#----------------------------------------
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
