
import numpy as np

class PopulationModel:

    iteration = 0

    def __init__(self, nodes, tmat):
        self.nodes = nodes
        self.tmat = tmat
        self.history = PopulationHistory()
        self.history.push(self.nodes)

    def __str__(self):
        return str(PopulationStrings(self.iteration, self.nodes))

    def iterate(self, count=1):
        for _ in range(count):
            self.nodes = np.matmul(self.tmat, self.nodes)
            self.history.push(self.nodes)
        self.iteration += count

class PopulationHistory:

    timesets = []

    def push(self, nodes):
        self.timesets.append(nodes)

    def __getat__(self, time):
        return self.timesets[time]

    def __str__(self):
        string = ""
        for i in range(len(self.timesets)):
            string += str(PopulationStrings(i, self.timesets[i])) + '\n'
        return string

class PopulationStrings:

    def __init__(self, iteration, nodes):
        self.iteration = iteration
        self.nodes = nodes

    def __str__(self):
        format = "{itr}: nodes={nodes} => sum={sum}"
        return format.format(itr=self.iteration, nodes=self.nodes, sum=np.sum(self.nodes))
