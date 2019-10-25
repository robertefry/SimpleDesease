
import numpy as np

class PopulationModel:

    iteration = 0

    def __init__(self, nodes, tmat):
        self.nodes = nodes
        self.tmat = tmat

    def __str__(self):
        format = "{itr}: nodes={nodes} => sum={sum}"
        return format.format(itr=self.iteration, nodes=self.nodes, sum=np.sum(self.nodes))

    def iterate(self, count=1):
        for _ in range(count):
            self.nodes = np.matmul(self.tmat, self.nodes)
        self.iteration += count
