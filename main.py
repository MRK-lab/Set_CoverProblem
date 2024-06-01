import random
import itertools # Bu modül, özellikle kombinatoryal yapıların oluşturulması ve manipülasyonu için çok faydalıdır.

# {1,2,3,4,5,6}
# {4,6}
# {1,2,3,5}
# {2,3,5}
# {1} -> {1}


def generate_universe_and_subsets(universe_size, num_subset, min_set_size, max_set_size):
    universe= set(range(1, universe_size+1))

    subsets = []
    remaining_elements = set(universe)

    while remaining_elements:
        set_size= random.randint(min_set_size, max_set_size)
        new_subset= set(random.sample(list(remaining_elements), min(set_size, len(remaining_elements))))
        subsets.append(new_subset)
        remaining_elements -= new_subset

    for _ in range(num_subset - len(subsets)):
        set_size = random.randint(min_set_size, max_set_size)
        new_subset = set(random.sample(list(universe), set_size))
        subsets.append(new_subset)

    return universe, subsets

universe, subsets = generate_universe_and_subsets(universe_size=80, num_subset=50, min_set_size=2, max_set_size=15)

#print(universe)
#for s in subsets:
#    print(s)


# U= {1,2,3,4,5,6}
# s = {1,2} {2} {3,4,5} {1,3,5} {5,6} {1,6}
#

#################################################
def brute_force_set_cover(universe, sets):
    n = len(sets)

    # O(n *2^n)
    for  i in range(1, n+1):
        for subset in itertools.combinations(sets, i):
            if set.union(*subset) == universe:
                return subset

#solution= brute_force_set_cover(universe, subsets)

#print(universe)
#for s in subsets:
#    print(s)

#print(solution)
#print(len(solution))
#print(set.union(*solution) == universe)


########################################
# max kesisim aranir
def greedy_set_cover(universe, sets):
    uncovered = universe.copy()
    solution = []

    while uncovered:
        # O(n * C)
        best_set=max(sets, key=lambda s: len(s & uncovered))
        solution.append(best_set)
        uncovered -= best_set

    return solution

solution= greedy_set_cover(universe, subsets)
print(solution)
print(len(solution))

solution=brute_force_set_cover(universe, subsets)
print(solution)
print(len(solution))

