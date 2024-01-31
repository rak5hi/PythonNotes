####################################################
x = 0.3
y = 0.1 + 0.2

print(x)
print(y)
print(x == y,end='\n\n\n')
####################################################
def compare_float(a: float,b: float, tolarence: float):
    absolute = abs(a - b)
    print(f'{a} - {b} = {a-b}')
    return absolute < tolarence

first = 0.8
second = 0.1 + 0.7

print(compare_float(first, second, tolarence=1e-10))  #0.0000000001
####################################################
