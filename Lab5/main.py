from graph.incidence_matrix_graph import IncidenceMatrixGraph
import algorithms

'''Module contains actions required for lab'''


def union(g1, g2):
    '''Returns graph containing edges of both graphs passed. Required for uniting results of Prim's algorithm and Kruskal's algorithm

    Args:
        g1 (IncidenceMatrixGraph): first graph
        g2 (IncidenceMatrixGraph): second graph

    Returns:
        IncidenceMatrixGraph: result of uniting'''

    if g1.vertex_count != g2.vertex_count:
        raise Exception('Graphs must have equal amount of vertices')

    result = IncidenceMatrixGraph()

    for i in range(g1.vertex_count):
        result.insert_vertex()

    for i in range(g1.vertex_count - 1):
        for j in range(i+1, g1.vertex_count):
            if g1.matrix[i][j] is not None:
                result.insert_edge([i, j], g1.matrix[i][j])
            elif g2.matrix[i][j] is not None:
                result.insert_edge([i, j], g2.matrix[i][j])

    return result


def jobs_employees_problem(speeds, preferences):
    '''Solves jobs and employees problem using Gale-Shapley algorithm and prints the solution

    Args:
        speeds (list): matrix of jobs with speed of doing that job for each employee
        preferences (list): matrix of employees' job preferences regular for Gale-Shapley algorithm

    Example:
        To represent infinite time in speeds matrix (employee cannot do this job) import math module and use math.inf
        or do 'from math import inf' and use just inf

        speeds = [
            [5,1,inf],
            [3,0,7],
            [2, 2, 3]
        ]

        prefs = [
            [0,1,2],
            [2,1,0],
            [2,0,1]
        ]

        jobs_employees_problem(speeds, prefs)'''

    employee_prefs = [[i for i,v in sorted(enumerate(job), key=lambda kv: kv[1])] for job in speeds]
    productivity_first_map = algorithms.gale_shapley(employee_prefs, preferences)
    print('Distribution when productivity is first:', {i: v for i, v in enumerate(productivity_first_map)})

    productivity_first_sum = 0
    for job, employee in enumerate(productivity_first_map):
        calculated_time = speeds[job][employee]
        min_time = min(speeds[job])
        productivity_first_sum += abs(calculated_time - min_time)

    print('Productivity first sum:', productivity_first_sum)

    preference_first_map = algorithms.gale_shapley(preferences, employee_prefs)
    print('Distribution when preference is first', {i: v for i, v in enumerate(preference_first_map)})

    preference_first_sum = 0
    for employee, job in enumerate(preference_first_map):
        preference_first_sum += preferences[employee].index(job)

    print('Preference first sum:', preference_first_sum)
