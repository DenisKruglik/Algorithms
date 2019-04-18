import random
import math
import copy


def delta(u, w, x, y, z):
    return abs((w*(x**2)*(z**2)+(w**2)*y+(u**2)*(w**2)*z+y+(w**2)*y*z) + 38)


mutation_probability = 0.05
population_size = 8
pairs_amount = 2
subgroup_size = 2


def run():
    # Start population
    population = []
    for i in range(population_size):
        population.append(tuple([random.randint(-100, 100) for j in range(5)]))

    highscore = None
    while True:
        # Selection
        subgroups = []
        pop = copy.deepcopy(population)
        random.shuffle(pop)
        for i in range(math.ceil(len(pop) / subgroup_size)):
            ind = i * subgroup_size
            subgroups.append(population[ind:ind + subgroup_size])

        best_candidates = []

        for group in subgroups:
            deltas = list(map(lambda ind: delta(*ind), group))
            best_result = min(deltas)
            best = group[deltas.index(best_result)]
            if highscore is None or best_result < delta(*highscore):
                highscore = best
                print(highscore, 'Delta = %s' % delta(*highscore))
                if delta(*highscore) == 0: return highscore
            best_candidates.append(best)

        pairs = [[best_candidates[i], best_candidates[j]] for i in range(len(best_candidates) - 1) for j in
                 range(i + 1, len(best_candidates))]

        # Crossingover
        descendants = []
        for pair in pairs:
            descendants.append([pair[0][i] if i < 2 else pair[1][i] for i in range(5)])
            descendants.append([pair[1][i] if i < 2 else pair[0][i] for i in range(5)])
            descendants.append([pair[1][i] if 1 < i < 3 else pair[0][i] for i in range(5)])
            descendants.append([pair[0][i] if 1 < i < 3 else pair[1][i] for i in range(5)])

        # Mutation
        for child in descendants:
            for ind, bit in enumerate(child):
                if random.random() < mutation_probability:
                    child[ind] = random.randint(-100, 100)

        # Replacing
        deltas = map(lambda child: delta(*child), descendants)
        deltas = {i: v for i, v in enumerate(deltas)}
        keys = sorted(deltas, key=lambda i: deltas[i])
        population = [descendants[i] for i in keys[:population_size]]


if __name__ == '__main__':
    run()