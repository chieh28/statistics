
import math
import random

class Binomial_dist():

    def __init__(self, p):
        self.p = p

    def mean(self):
        return self.p
    
    def var(self, n):
        _var = n * self.p * (1 - self.p)
        return _var
    
    def std(self, n):
        _std = self.var(n) ** 0.5
        return _std
    
    def probability(self, n, k):
        pro = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k))) * (self.p ** k) * ((1 - self.p) ** (n - k))
        return pro
    
    def sample(self, size):
        _sample = [0] * size

        for i in range(size):
            rand = random.random()
            if rand <= self.p:
                _sample[i] = 0
            else:
                _sample[i] = 1

        return _sample
    
binomial = Binomial_dist(0.7)
print(binomial.mean())
print(binomial.var(10))
print(binomial.std(10))
print(binomial.probability(10, 5))
print(binomial.sample(10))