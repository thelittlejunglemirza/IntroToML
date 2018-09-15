import numpy as np

def example(x):
    return np.sum(x**2)


def example_grad(x):
    print(type(x))
    return 2*x

def foo(x):
    result = 1
    λ = 4 # this is here to make sure you're using Python 3
    for x_i in x:
        result += x_i**λ
    return result

def foo_grad(x):
    myList = []
    a = 3
    b = 4
    for x_i in x:
        myList.append(b * x_i ** a)
    return np.array(myList)

def bar(x):
    return np.prod(x)

## approch 2 faster method
def bar_grad(x):
    myList =[]
    for x_i in x:
        tmp_arr = x
        idx = np.argwhere(tmp_arr == x_i)
        tmp_arr = np.delete(tmp_arr, idx)
        myList.append(np.prod(tmp_arr))
    return np.array(myList)

## approach 1 n^2 sorta slow on big input
# def bar_grad(x):
#     myList =[]
#     for x_i in x:
#         temp = 1
#         for x_j in x:
#             if (x_i != x_j):
#                 temp *= x_j
#         myList.append(temp)
#     return np.array(myList)
