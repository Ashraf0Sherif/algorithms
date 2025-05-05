import random
import numpy as np

def genetic_algorithm(fitness_function, gene_length, population_size=100, 
                     generations=50, mutation_rate=0.01, elite_size=10):
    population = [
        ''.join(random.choice('01') for _ in range(gene_length))
        for _ in range(population_size)
    ]
    
    for generation in range(generations):
        fitness_scores = [fitness_function(individual) for individual in population]
        
        population_fitness = list(zip(population, fitness_scores))
        
        population_fitness.sort(key=lambda x: x[1], reverse=True)
        
        if generation % 10 == 0:
            print(f"Generation {generation}: Best fitness = {population_fitness[0][1]}")
        
        elites = [individual for individual, _ in population_fitness[:elite_size]]
        
        total_fitness = sum(fitness_scores)
        selection_probs = [fitness/total_fitness for fitness in fitness_scores]
        
        new_population = elites.copy()
        
        while len(new_population) < population_size:
            parent1 = population[np.random.choice(range(population_size), p=selection_probs)]
            parent2 = population[np.random.choice(range(population_size), p=selection_probs)]
            
            crossover_point = random.randint(1, gene_length - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            
            child_genes = list(child)
            for i in range(gene_length):
                if random.random() < mutation_rate:
                    child_genes[i] = '1' if child_genes[i] == '0' else '0'
            
            child = ''.join(child_genes)
            new_population.append(child)
        
        population = new_population
    
    final_fitness = [fitness_function(individual) for individual in population]
    best_idx = final_fitness.index(max(final_fitness))
    
    return population[best_idx], final_fitness[best_idx]

if __name__ == "__main__":
    def fitness_function(individual):
        return individual.count('1')
    
    gene_length = 20
    
    best_individual, best_fitness = genetic_algorithm(
        fitness_function=fitness_function,
        gene_length=gene_length,
        generations=100
    )
    
    print("\nBest individual:", best_individual)
    print("Best fitness:", best_fitness)