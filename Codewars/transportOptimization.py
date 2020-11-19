from numpy import array

def minimum_transportation_price(suppliers, consumers, costs):
    costs_array = numpy.array(costs)
    return

def calculate_minimal_costs_method(suppliers, consumers, costs):
    iterations = len(suppliers) + len(consumers) - 1
    for i in range(iterations):
        min_cost_position = get_minimal_cost_position(costs)
    pass

def fill_cell(suppliers, consumers, *pargs):
    pass

def get_minimal_cost_position(costs):
    minimal_cost = costs.min()
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if costs[i,j] == minimal_cost:
                return i, j
    