class Chromosome:
    gene = []

    def __init__(self, val):
        for i in range(len(val)):
            self.gene[i] = val[i]
