import random

population = [
    random.randint(0, 100)
    for _ in range(10)
]

def fitness(x):
    return -(x - 75) ** 2

for generation in range(50):

    population.sort(key=fitness, reverse=True)

    parents = population[:4]

    new_population = parents.copy()

    while len(new_population) < 10:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2

        if random.random() < 0.2:
            child += random.randint(-5, 5)

        child = max(0, min(100, child))
        new_population.append(child)

    population = new_population

print(max(population, key=fitness))