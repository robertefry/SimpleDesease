
import numpy as np

## vector of population nodes
# nodes[0]: susceptible
# nodes[1]: infected
# nodes[2]: recovered
# nodes[3]: dead
nodes = [1, 0, 0, 0]

## transition matrix
tmat = [
    [0.95, 0.00, 0.00, 0.00],
    [0.05, 0.84, 0.00, 0.00],
    [0.00, 0.15, 1.00, 0.00],
    [0.00, 0.01, 0.00, 1.00]
]

def printmodel(iteration, nodes):
    format = "{itr}: nodes={nodes} => sum={sum}"
    string = format.format(itr=iteration, nodes=nodes, sum=np.sum(nodes))
    print(string)

def main():

    ## use the global model tensors
    global nodes
    global tmat

    ## print the initial population
    printmodel(0, nodes)

    ## iterate over time
    for i in range(50):
        nodes = np.matmul(tmat, nodes)
        printmodel(i+1, nodes)

if __name__ == "__main__":
    main()
