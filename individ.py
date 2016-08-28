# coding=utf-8
import random

from utils import coder


class Individ:
    def __init__(self):
        self.alleles = []
        for i in range(0, 4):
            self.alleles.append(i)
        self.fitness = -1

    def generate_individ(self, n):
        """
        Генерирует особь
        """
        for j in xrange(n):
            self.alleles[j] = coder.code(random.uniform(-10, 10))

        return self.alleles

# class Population:
#     def __init__(self, population):
#         self.population = population
#
#     def get_result(self):
#         population = self.population
#         for i in range(0, len(population)):
#             population[]