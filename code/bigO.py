import numpy as np
import time as t

def func1(N):
    for i in range(N):
        print("Hello!")

def func2(N):
    x = np.zeros(N)
    x += 1000
    return x

def func3(N):
    x = np.zeros(1000)
    x = x * N
    return x

def func4(N):
    x = 0
    for i in range(N):
        for j in range(i,N):
            x += (i*j)
    return x

def func5(N):
    for i in range(N):
        1 + 1
    print('func5 done')


start_time = t.time()
print('working1');
func2(10000000000)
print('done1: =====> %s seconds' % (t.time() - start_time))

new_start_time = t.time()
print('working2');
func3(10000000000)
print('done2: =====> %s seconds' % (t.time() - new_start_time))
