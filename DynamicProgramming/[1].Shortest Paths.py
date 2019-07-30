

def read_graph(in_file):
    """ Read in the graph from the data file.  The graph is stored
    as a dictionary, where the keys are the nodes, and the values
    are a list of pairs (d, c), where d is a node and c is a number.
    If (d, c) is in the list for node n, then d can be reached from
    n at cost c.
    """
    graph = {}
    infile = open(in_file)
    for line in infile:
        elements = line.split(',')
        node = elements.pop(0)
        graph[node] = []
        if node != 'node99':
            for element in elements:
                destination, cost = element.split()
                graph[node].append((destination, float(cost)))
    infile.close()
    return graph


def update_J(J, graph):
    "The Bellman operator."
    next_J = {}
    for node in graph:
        if node == 'node99':
            next_J[node] = 0
        else:
            next_J[node] = min(cost + J[dest] for dest, cost in graph[node])
    return next_J


def print_best_path(J, graph):
    """ Given a cost-to-go function, computes the best path.  At each node n,
    the function prints the current location, looks at all nodes that can be
    reached from n, and moves to the node m which minimizes c + J[m], where c
    is the cost of moving to m.
    """
    sum_costs = 0
    current_location = 'node0'
    while current_location != 'node99':
        print(current_location)
        running_min = 1e100  # Any big number
        for destination, cost in graph[current_location]:
            cost_of_path = cost + J[destination]
            if cost_of_path < running_min:
                running_min = cost_of_path
                minimizer_cost = cost
                minimizer_dest = destination
        current_location = minimizer_dest
        sum_costs += minimizer_cost

    print('node99\n')
    print('Cost: ', sum_costs)


# Main loop
graph = read_graph('graph.txt')
M = 1e10
J = {}
for node in graph:
    J[node] = M
J['node99'] = 0

while True:
    next_J = update_J(J, graph)
    if next_J == J:
        break
    else:
        J = next_J

print_best_path(J, graph)

