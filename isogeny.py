from j_invariants import *
import random
import math

# Set the range for the circular layout
circle_center = (925, 525)  # Center of the circle within the x and y range
radius = 400  # Radius for circular layout

def calculate_position_on_circle(index, total_nodes):
    """Calculate the x, y position of each node in a circular layout."""
    angle = 2 * math.pi * index / total_nodes  # Evenly distribute nodes around the circle
    x = circle_center[0] + radius * math.cos(angle)
    y = circle_center[1] + radius * math.sin(angle)
    return (int(x), int(y))

def single_isogeny_graph_n(param_a, param_b, j_inv, n, index, total_nodes):
    E = EllipticCurve(F, (param_a, param_b))
    ker_n = kernel_of_isogeny(E, n)
    print(ker_n)
    connections = []
    for ker in ker_n:
        for b in F:
            isogeny = EllipticCurveIsogeny(E, kernel=ker)
            E_isogeny = isogeny.codomain()
            j_inv_a = j_invariant(E_isogeny.a4(), E_isogeny.a6())
            print(E_isogeny, j_inv_a)
            if is_supersingular_curve(j_inv_a) and j_inv_a not in connections:
                connections.append(str(j_inv_a))        
                break
            else:
                continue
    if connections:
        print(f"{j_inv} to {connections}")
        pos = calculate_position_on_circle(index, total_nodes)  # Calculate circular position
        return {"pos": pos, "connections": connections}
  
    
def isogenies():
    nodes = {}
    total_nodes = len(params)
    for index, param in enumerate(params):
        j_inv = j_invariant(param[0], param[1])
        nodes[str(j_inv)] = single_isogeny_graph_n(param[0], param[1], j_inv, 3, index, total_nodes)
         
    print(nodes)
    print(len(nodes))
    return nodes

isogenies()
