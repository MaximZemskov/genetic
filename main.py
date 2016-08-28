# coding=utf-8

import random
import time

from utils import coder
from individ import Individ


def generate_individ(n):
    """
    Генерирует особь
    """
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

    return population


def main():
    N = 20  # размер начальной популяции
    n = 4  # количество особей
    # population = generate_initial_population(N, n)
    #
    # # for pop in population:
    # #     print pop
    #
    # print population
    population = []
    for i in xrange(N):
        individ = Individ()
        new_individ = generate_individ(n)
        for i in xrange(n):
            individ.alleles[i] = new_individ[i]
        population.append(individ)

    for pop in population:
        print pop.alleles[0]

    print population[10].fitness


if __name__ == '__main__':
    main()
