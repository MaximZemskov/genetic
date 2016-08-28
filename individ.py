# coding=utf-8
import random

from utils import coder


class Individ:
    def __init__(self, N):
        self.alleles = []
        for i in range(0, 4):
            self.alleles.append(i)
        self.fitness = -1
        self.MAX_POP = N
        self.likelihoods = -1

    def generate_individ(self, n):
        """
        Генерирует особь
        """
        for j in xrange(n):
            self.alleles[j] = coder.code(random.uniform(-10, 10))

        return self.alleles

    def fitness_count(self):
        total = coder.decode(self.alleles[0]) - 2 * coder.decode(self.alleles[1]) + coder.decode(
            self.alleles[2]) + 4 * coder.decode(self.alleles[3])
        self.fitness = abs(total - 13.5)
        return self.fitness

    def create_fitness(self):
        for i in range(0, self.MAX_POP):
            fitness = self.fitness_count()
            if fitness == 0:
                return i
        return 0

        # class Population:
        #     def __init__(self, population):
        #         self.population = population
        #
        #     def get_result(self):
        #         population = self.population
        #         for i in range(0, len(population)):
        #             population[]
