import random

# Définition de la fonction pour évaluer la solution
def evaluate_solution(solution, weights, values, max_weight):
    total_weight = sum(solution[i] * weights[i] for i in range(len(solution)))
    total_value = sum(solution[i] * values[i] for i in range(len(solution)))
    if total_weight > max_weight:
        return -1  # Pénalité si le poids total dépasse la capacité maximale
    else:
        return total_value

# Algorithme Hill Climbing
def hill_climbing(weights, values, max_weight, iterations):
    best_solution = [0] * len(weights)  # Initialiser avec aucun objet dans le sac
    best_value = evaluate_solution(best_solution, weights, values, max_weight)
    
    for _ in range(iterations):
        # Générer une solution voisine en modifiant un objet aléatoire
        index = random.randint(0, len(weights) - 1)
        new_solution = best_solution.copy()
        new_solution[index] = 1 if new_solution[index] == 0 else 0
        
        # Évaluer la nouvelle solution
        new_value = evaluate_solution(new_solution, weights, values, max_weight)
        
        # Mettre à jour la meilleure solution si la nouvelle solution est meilleure
        if new_value > best_value:
            best_solution = new_solution
            best_value = new_value
            
    return best_solution, best_value

# Exemple d'utilisation
if __name__ == "__main__":
    weights = [5, 10, 15, 7, 3]
    values = [10, 30, 20, 5, 8]
    max_weight = 20
    iterations = 1000
    
    best_solution, best_value = hill_climbing(weights, values, max_weight, iterations)
    
    print("Meilleure solution trouvée:", best_solution)
    print("Valeur de la meilleure solution:", best_value)
