# coding=utf-8

import random
import sys
import time

from utils import coder
from individ import Individ

MAX_POP = 20


def generate_individ(n):
    """
    Генерирует особь
    """
    individ = []
    for j in xrange(n):
        individ.append(coder.code(random.uniform(-10, 10)))
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
    parrent_pool = []


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

    child = parent_a[:separator] + parent_b[separator:]
    return child


def main():
    N = 20  # размер начальной популяции
    n = 4  # количество особей

    population = generate_initial_population(N, n)

    for pop in population:
        print pop

    for pop in population:
        for i in xrange(len(pop)):
            sys.stdout.write(str(coder.decode(pop[i])) + ", ")
        print ""


if __name__ == '__main__':
    main()
