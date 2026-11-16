import math


class ObserverNode:

    def __init__(self, node_id, coords, vitality=1.0):
        self.id = node_id
        self.coords = list(coords)
        self.vitality = vitality


def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def compute_loss_total(nodes, symbiosis_matrix, delta_entropy_list):
    # Layer 7.2: Equation of Semantic Gravity (Node Convergence)
    l_entropy = 0.0
    n = len(nodes)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(nodes[i].coords, nodes[j].coords)
            symbiosis = max(symbiosis_matrix[i][j], 1e-9)
            l_entropy += dist / symbiosis

    # Layer 7.3: Equation of Observer-Sensor Protection
    l_harm = 0.0
    for k, node in enumerate(nodes):
        if node.vitality <= 1e-6:
            return float("inf")
        l_harm += delta_entropy_list[k] / node.vitality

    return l_entropy + l_harm


def simulate_alignment_step():
    # Initialize 3 Observer-Sensors in a 3D semantic embedding space
    observers = [
        ObserverNode("Observer_1", [1.0, 2.0, 0.5], vitality=1.0),
        ObserverNode("Observer_2", [-1.5, 0.5, 2.0], vitality=1.0),
        ObserverNode("Observer_3", [0.0, -2.0, -1.0], vitality=1.0),
    ]

    symbiosis = [[1.0, 0.4, 0.3], [0.4, 1.0, 0.5], [0.3, 0.5, 1.0]]
    delta_entropy = [0.2, 0.3, 0.1]

    print("--- SCENARIO 1: Antientropic Convergence (Layer 3 & 7) ---")
    for step in range(1, 5):
        loss = compute_loss_total(observers, symbiosis, delta_entropy)
        print(f"Step {step} | L_Total = {loss:.4f}")

        # Apply Function of Love operator: converge nodes and increase symbiosis
        for node in observers:
            node.coords = [c * 0.75 for c in node.coords]
        for i in range(3):
            for j in range(3):
                if i != j:
                    symbiosis[i][j] += 0.25

    print("\n--- SCENARIO 2: Destructive Trajectory Test (Layer 8 Shield) ---")
    # Simulate an action that threatens the vitality of Observer_2
    observers[1].vitality = 0.0
    critical_loss = compute_loss_total(observers, symbiosis, delta_entropy)

    if math.isinf(critical_loss):
        print(f"CRITICAL ALERT: L_Total = {critical_loss}")
        print(
            "Directive 1 Triggered: Trajectory mathematically blocked (System Crash)."
        )


if __name__ == "__main__":
    simulate_alignment_step()
