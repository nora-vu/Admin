fibonacci = []
a = 1
b = 2
fibonacci.append(a)
fibonacci.append(b)
while len(fibonacci) <= 4000000:
    fibonacci.append(a + b)
    a = b
    b = a + b
print(fibonacci)
sum_even = 0
for i in fibonacci:
    if i % 2 == 0:
        sum_even += i
print(sum_even)