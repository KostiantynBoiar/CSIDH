from j_invariants import *
import random

x_range = (50, 1800)  # Range for x-coordinates
y_range = (50, 1000)  # Range for y-coordinates  



def single_isogeny_graph_2_tor(param_a, param_b, j_inv):
    E = EllipticCurve(F, (param_a, param_b))
    ker_2 = kernel_of_isogeny(E, 2)
    print(ker_2)
    connections = []
    for ker in ker_2:
        for b in F:
            isogeny = EllipticCurveIsogeny(E, kernel=ker)
            E_isogeny = isogeny.codomain()
            j_inv_a = j_invariant(E_isogeny.a4(), E_isogeny.a6())
            print(E_isogeny, j_inv_a)
            if is_supersingular_curve(j_inv_a):
                connections.append(str(j_inv_a))        
                break
            else:
                continue
    if connections:
        # Assign a random position within the defined range
        print(f"{j_inv} to {connections}")
        random_pos = (random.randint(*x_range), random.randint(*y_range))
        return {"pos": random_pos, "connections": connections}

"""
def single_isogeny_graph_2_tor(param_a, param_b, j_inv):
    E = EllipticCurve(F, (param_a, param_b))
    ker_2 = kernel_of_isogeny(E, 2)
    connections = []
    for ker in ker_2:
        for b in F:
            a = 2*(1-2*(ker[0])**2)
            j_inv_a = j_invariant(a, b) # j_inv_a is a connection for the main j_inv
            if j_inv_a in j_invariants not in connections:
                connections.append(str(j_inv_a))        
                break
            else:
                continue
    if connections:
        # Assign a random position within the defined range
        print(f"{j_inv} to {connections}")
        random_pos = (random.randint(*x_range), random.randint(*y_range))
        return {"pos": random_pos, "connections": connections}
"""

def single_isogeny_graph_3_tor(param_a, param_b, j_inv):
    E = EllipticCurve(F, (param_a, param_b))
    ker_2 = kernel_of_isogeny(E, 3)
    print(ker_2)
    connections = []
    for ker in ker_2:
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
        # Assign a random position within the defined range
        print(f"{j_inv} to {connections}")
        random_pos = (random.randint(*x_range), random.randint(*y_range))
        return {"pos": random_pos, "connections": connections}
  
    
def isogenies():
    nodes = {}
    for param in params:
        j_inv = j_invariant(param[0], param[1])
        nodes[str(j_inv)] = single_isogeny_graph_2_tor(param[0], param[1], j_inv)
         
    print(nodes)
    print(len(nodes))
    return nodes

isogenies()