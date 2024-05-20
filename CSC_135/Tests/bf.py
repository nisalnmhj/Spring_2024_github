import math

def binomial_probability(n, x, p):
    return (math.comb(n, x)) * (p ** x) * ((1 - p) ** (n - x))

n = 29
p = 0.01
total_probability = 0

for x in range(16):
    total_probability += binomial_probability(n, x, p)

print("Summative probability that any up to 15 users are transmitting:", total_probability)
