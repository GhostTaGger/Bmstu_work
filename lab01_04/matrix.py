from random import randint
from functions import matrix_multiplication, draw_graph
from decorators import get_usage_time
import numpy as np

A_ = []
B_ = []

N_ = 20 - 4
step_n = N_
end_n = 10**2 * N_
start_n = 1
x_vec = range(1, 10**2*N_, N_)
y_vec = []
for step in range(1, end_n, step_n):
    A_ = np.random.rand(step, step)
    B_ = np.random.rand(step, step)
    func = get_usage_time(number=5, ndigits=5)(matrix_multiplication)
    y_vec.append(func(A_,B_))
name = 'matrix multiplication'
draw_graph(x_vec,y_vec,name)