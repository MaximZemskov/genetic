# coding=utf-8

import random
import time

from utils import coder
from individ import Individ

MAX_POP = 20

population = []


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
    for i in xrange(N):
        population.append(generate_individ(n))

    return population


# def create_fitness(self):
#     for i in range(0, self.MAX_POP):
#         fitness = self.fitness_count()
#         if fitness == 0:
#             return i
#     return 0

def create_fitness():
    for i in range(0, MAX_POP):
        fitness = population[i].fitness_count()
        if fitness == 0:
            return i
    return 0

# float CDiophantine::MultInv() {
# 	float sum = 0;
#
# 	for(int i=0;i<MAXPOP;i++) {
# 		sum += 1/((float)population[i].fitness);
# 	}
#
# 	return sum;
# }

def mult_inv():
    summa = 0

    for i in range(0, MAX_POP):
        summa += 1.0 / population[i].fitness

    return summa

#
# void CDiophantine::GenerateLikelihoods() {
# 	float multinv = MultInv();
#
# 	float last = 0;
# 	for(int i=0;i<MAXPOP;i++) {
# 		population[i].likelihood = last = last + ((1/((float)population[i].fitness) / multinv) * 100);
# 	}
# }


def generate_like_li_hoods():
    multinv = mult_inv()

    last = 0
    for i in range(0, MAX_POP):
        population[i].likelihoods = last = last + ((1.0 / population[i].fitness) / multinv) * 100



def get_index(val):
    last = 0
    for i in range(0, MAX_POP):
        if (last <= val) and (val <= population[i].likelihood):
            return i
        else:
            last = population[i].likelihood
    return 4

def main():
    N = 20  # размер начальной популяции
    n = 4  # количество особей

    fitness = -1
    # population = generate_initial_population(N, n)
    #
    # # for pop in population:
    # #     print pop
    #
    # print population

    # generate initial population

    for i in xrange(N):
        individ = Individ(N)
        new_individ = generate_individ(n)
        for i in xrange(n):
            individ.alleles[i] = new_individ[i]
        population.append(individ)

    # оцениваем приспособленность

    fitness = create_fitness()

    if not fitness:
        print "Solution found"
        print fitness
    else:
        iterations = 0
        while (iterations != 1000) or (fitness != 0):



    # for pop in population:
    #     print pop.alleles[0]
    #
    # print population[10].fitness


if __name__ == '__main__':
    main()
