# coding=utf-8

import random
import time

from utils import coder

def generate_individ(n):
    individ = []
    for j in xrange(n):
        individ.append(coder.code(random.uniform(-10, 10)))
        # individ.append(random.uniform(-10, 10))
    return individ


def generate_initial_population(N, n):
    """
    N - размер популяции
    n - количество хромосом
    """
    population = []
    for i in xrange(N):
        population.append(generate_individ(n))

    for pop in population:
        print pop


def main():
    N = 20  # размер начальной популяции
    n = 4  # количество особей
    generate_initial_population(20, 4)


if __name__ == '__main__':
    main()
