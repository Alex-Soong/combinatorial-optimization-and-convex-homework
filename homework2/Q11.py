import numpy as np


def f(x):
    return x[0] ** 2 + 4 * x[1] ** 2 - 4 * x[0] - 8 * x[1] 


def gradient(x):
    return np.array([2 * x[0] - 4, 8 * x[1] - 8])


def momentum(x_init, grad_func, lr=0.01, gamma=0.9, max_iter=1000, tol=1e-6):
    x = x_init.copy()
    v = np.zeros_like(x)
    k = 0
    while k < max_iter:
        grad = grad_func(x)
        v = gamma * v + lr * grad
        x_new = x - v
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
        k += 1
    return x, k


x_init = np.array([1 / 10, 1])
x_min, iterations = momentum(x_init, gradient)
x_min = np.round(x_min, 2)
y_min = np.round(f(x_min), 2)
print("最小值点：", x_min)
print("最小值：", y_min)
print("迭代次数：", iterations)
