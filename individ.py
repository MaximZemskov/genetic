# coding=utf-8
import random

from utils import coder


class Individ:
    def __init__(self, N):
        self.alleles = []
        for i in range(0, 4):
            self.alleles.append(i)
        self.MAX_POP = N
        self.fitness = random.random()

    def generate_individ(self, n):
        """
        Генерирует особь
        """
        for j in xrange(n):
            self.alleles[j] = coder.code(random.uniform(-10, 10))

        return self.alleles
