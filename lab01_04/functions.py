from random import randint
from decorators import get_usage_time
import functools
import timeit
import typing
import matplotlib.pyplot as plt
import numpy as np

def matrix_multiplication(matrix_a,matrix_b):
    return np.dot(matrix_a,matrix_b)


def const_func(rand_vec):
    return rand_vec

def sum_func(rand_vec):
    tries_ = 5
    sum_ = 0
    for i in rand_vec:
        sum_ += i
   # print(sum_/len(rand_vec))


def draw_graph(items, times,name):
    fig = plt.plot(items, times, 'bo-')
    plt.title(name)
    ax = plt.gca()
    ax.set_xlabel('Number of elements, $n$ ')
    ax.set_ylabel('Time, sec')
    plt.show()


def gorner_estimate(rand_vec):
    N_ = 16
    x = 1.5 * N_
    polynome = 0
    for vec_elem in rand_vec[::-1]:
        polynome = vec_elem + x * polynome


def simple_max_search(rand_vec):
    max = 0
    for vec_elem in rand_vec:
        if max < vec_elem:
            max = vec_elem