from functions import const_func, draw_graph, gorner_estimate, simple_max_search, sum_func
from random import random, randint
from decorators import get_usage_time
import timeit
N_ = 20 - 4
step_n = N_ * 10**2
end_n = 10**5 * N_
start_n = 1
x_vec = []
y_vec = []
rand_vec = [randint(1, 100) for _ in range(1, end_n)] # создаем вектор длинной 1:end_n
for step in range(1, end_n,step_n):
    tmp_vec = rand_vec[1:step]
    func = get_usage_time(number=5, ndigits=5)(sum_func) # gorner_estimate, simple_max_search, const_func
#    print(tmp_vec)
    y_vec.append(func(tmp_vec))
name = 'Sum function'
x_vec = range(1, 10**5*N_, 100*N_)
draw_graph(x_vec,y_vec,name)