
import matplotlib.pyplot as plt
import numpy as np

class PopulationModel:

    def __init__(self, nodes, tmat):
        self.nodes = nodes
        self.tmat = tmat
        self.iteration = 0
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

    def __init__(self):
        self.timesets = []

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

class PopulationPlotter:

    def __init__(self, history):
        self.iterations = len(history.timesets) - 1
        self.nodesets = np.transpose(history.timesets)
        self.labels = ["node{0}".format(i) for i in range(len(self.nodesets))]

    def plot(self):
        for i in range(len(self.nodesets)):
            percent = "{:02.1f}%".format(self.nodesets[i][self.iterations]*100).zfill(5)
            label = "{percent} {label}".format(label=self.labels[i], percent=percent)
            plt.plot(self.nodesets[i], label=label)
        plt.xlabel("iteration")
        plt.ylabel("percentage")
        plt.legend(loc='best')
        plt.show()
