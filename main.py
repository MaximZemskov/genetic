# coding=utf-8

import random
import sys
import time

from utils import coder
from individ import Individ

MAX_POP = 20


# def generate_individ(n):
#     """
#     Генерирует особь
#     """
#     individ = Individ()
#     for j in xrange(n):
#         individ.append(coder.code(random.uniform(-10, 10)))
#     return individ


def generate_initial_population(N, n):
    """
    N - размер популяции
    n - количество хромосом
    """
    population = []

    for i in xrange(N):
        individ = Individ(N)
        individ.generate_individ(n)
        population.append(individ)

    return population


def breed():
    """
    скрещивание
    :return:
    """
    pass


def selection(population):
    """
    создание родительского пулла
    :return:
    """
    parent_pool = []

    i = 0
    while len(parent_pool) != MAX_POP:
        if i == MAX_POP - 1:
            i = 0
        chance = random.random()
        if chance < population[i].fitness:
            parent_pool.append(population[i])
        i += 1

    return parent_pool


def mutation(chrom):
    """
    мутация.
    С вероятностью 10 процентов заменяет значение аллели на противоположное
    :param chrom:
    :return:
    """
    chance = 0.1  # шанс мутации
    chrom = list(chrom)
    for i in xrange(len(chrom)):
        if random.random() < chance:
            if chrom[i] == '1':
                chrom[i] = '0'
            elif chrom[i] == '0':
                chrom[i] = '1'
    chrom = ''.join(chrom)
    return chrom


def crossover(parent_a, parent_b, separator=None):
    """
    скрещивание методом кроссовера
    сепаратор можно передать как аргумент или он автоматически определится во время работы функции
    :param parent_a:
    :param parent_b:
    :param separator:
    :return:
    """
    n = 4  # количество хромосом в особи

    if not separator:
        separator = random.randint(1, n - 1)  # точка разделения для скрещивания

    child_1 = parent_a[:separator] + parent_b[separator:]
    child_2 = parent_b[:separator] + parent_a[separator:]
    return child_1, child_2


def main():
    N = MAX_POP  # размер начальной популяции
    n = 4  # количество особей

    population = generate_initial_population(N, n)

    for pop in population:
        print pop.alleles

    print ""
    parent_pool = selection(population)
    for pop in parent_pool:
        print pop.alleles


if __name__ == '__main__':
    main()
