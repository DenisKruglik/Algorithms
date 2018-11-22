from algorithms import floyd


def optimal_fire_station_location(graph):
    '''Returns a number of vertex which would be an optimal position for a fire station

    Args:
        graph (IncidenceMatrixGraph): graph under consideration

    Returns:
        int: index of vertex'''
    distances = floyd(graph)
    min_weight = None
    optimum = None

    for i, row in enumerate(distances):
        max_weight = max(row)
        if min_weight is None or min_weight > max_weight:
            min_weight = max_weight
            optimum = i
    return optimum