
from model import PopulationModel

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

def main():

    ## define our population model
    model = PopulationModel(nodes, tmat)

    ## iterate over time
    model.iterate(50)

    ## print the population history
    print(str(model.history))

if __name__ == "__main__":
    main()
