from j_invariants import *

def single_isogeny_graph_2_tor(param_a, param_b, j_inv):
    E = EllipticCurve(F, (param_a, param_b))
    ker_2 = kernel_of_isogeny(E, 2)
    for ker in ker_2:
        for b in F:
            a = 2*(1-2*(ker[0])**2)
            j_inv_a = j_invariant(a, b)
            if j_inv_a in j_invariants:        
                print(f"{j_inv} to {j_inv_a}")
                break
            else:
                continue

def isogenies():
    for param in params:
        single_isogeny_graph_2_tor(param[0], param[1], j_invariant(param[0], param[1]))

isogenies()