from j_invariants import *
import random

def public_params_generator(param):
    """Generate a supersingular curve and return public parameters."""
    for b in F:
        try:
            E = EllipticCurve(F, (param[0], b))
            j_inv_of_E = j_invariant(param[0], b)
        except:
            E = EllipticCurve(F, (param, b))
            j_inv_of_E = j_invariant(param, b)

        if is_supersingular_curve(j_inv_of_E):
            # Generate two independent points on the same supersingular curve
            P = E.random_point()  # First point
            Q = E.random_point()  # Second point, independent of P
            print(f"Alice E = {E}, param = {param}, j_inv_of_E = {j_inv_of_E}, P = {P}, Q = {Q}")
            return E, P, Q  # Return the curve and the two points
    return None, None, None


def find_point_of_order(curve, order):
    """Find a point on the elliptic curve with the specified order."""
    while 1:  
        point = curve.random_point()
        if point.order() == order:
            return point
    return None




def compute_step(E, k, order):
    print(E.a4())
    E_C, P_C, Q_C = public_params_generator(E.a4())
    k_Q = k * Q_C
    S = P_C + k_Q
    if S.order() != order:
        S = find_point_of_order(E_C, 2)
    S_isogeny = EllipticCurveIsogeny(E_C, S)
    E_a1 = S_isogeny.codomain()
    E_a1_j = E_a1.j_invariant()
    return S_isogeny, E_a1, E_a1_j


def alice_step_public_gen():
    steps = []
    E_alice, alice_public_p, alice_public_q = public_params_generator(choice(params))
    
    # Check if valid public parameters are generated
    if not (E_alice and alice_public_p and alice_public_q):
        print("Error: Failed to generate valid public parameters for Alice.")
        return None
    print("Bob's public parameters: P_A =", alice_public_p, ", Q_A =", alice_public_q)
    
    # Alice's secret scalar
    k_0 = 11
    
    #step 0
    S_A_isogeny, E_A_a1, E_A_a1_j = compute_step(E_alice, k_0, 2)
    print(f'Isogeny phi0 = {S_A_isogeny},\n EC_phi0 = {E_A_a1},\n j-inv_phi0 = {E_A_a1_j}')
    steps.append(E_A_a1_j)
    #step 1
    k_1 = 8

    S_A_isogeny_1, E_A_a1_1, E_A_a1_j_1 = compute_step(E_A_a1, k_1, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_1},\n EC_phi1 = {E_A_a1_1},\n j-inv_phi1 = {E_A_a1_j_1}')
    steps.append(E_A_a1_j_1)


    #step 2
    k_2 = 4

    S_A_isogeny_2, E_A_a1_2, E_A_a1_j_2 = compute_step(E_A_a1_1, k_2, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_2},\n EC_phi1 = {E_A_a1_2},\n j-inv_phi1 = {E_A_a1_j_2}')
    steps.append(E_A_a1_j_2)


    #step 3
    k_3 = 2

    S_A_isogeny_3, E_A_a1_3, E_A_a1_j_3 = compute_step(E_A_a1_2, k_3, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_3},\n EC_phi1 = {E_A_a1_3},\n j-inv_phi1 = {E_A_a1_j_3}')
    steps.append(E_A_a1_j_3)

    final_E_alice, alice_public_p, alice_public_q = public_params_generator(E_A_a1_3.a4())
    alice_PK = E_alice.a4(), alice_public_p, alice_public_q
    return steps, alice_PK


def bob_steps_public_gen():
    steps = []
    E_bob, bob_public_p, bob_public_q = public_params_generator(choice(params))
    
    # Check if valid public parameters are generated
    if not (E_bob and bob_public_p and bob_public_q):
        print("Error: Failed to generate valid public parameters for Bob.")
        return None
    print("Bob's public parameters: P_A =", bob_public_p, ", Q_A =", bob_public_q)
    
    # Alice's secret scalar
    k_0 = 2
    
    #step 0
    S_A_isogeny, E_A_a1, E_A_a1_j = compute_step(E_bob, k_0, 2)
    print(f'Isogeny phi0 = {S_A_isogeny},\n EC_phi0 = {E_A_a1},\n j-inv_phi0 = {E_A_a1_j}')
    steps.append(E_A_a1_j)
    #step 1
    k_1 = 5

    S_A_isogeny_1, E_A_a1_1, E_A_a1_j_1 = compute_step(E_A_a1, k_1, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_1},\n EC_phi1 = {E_A_a1_1},\n j-inv_phi1 = {E_A_a1_j_1}')
    steps.append(E_A_a1_j_1)


    #step 2
    k_2 = 9

    S_A_isogeny_2, E_A_a1_2, E_A_a1_j_2 = compute_step(E_A_a1_1, k_2, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_2},\n EC_phi1 = {E_A_a1_2},\n j-inv_phi1 = {E_A_a1_j_2}')
    steps.append(E_A_a1_j_2)


    #step 3
    k_3 = 3

    S_A_isogeny_3, E_A_a1_3, E_A_a1_j_3 = compute_step(E_A_a1_2, k_3, 2)
    print(f'Isogeny phi1 = {S_A_isogeny_3},\n EC_phi1 = {E_A_a1_3},\n j-inv_phi1 = {E_A_a1_j_3}')
    steps.append(E_A_a1_j_3) 

    final_E_bob, bob_public_p, bob_public_q = public_params_generator(E_A_a1_3.a4())
    bob_PK = E_bob.a4(), bob_public_p, bob_public_q

    return steps, bob_PK


def public_key_generation():
    steps = []
    # Generate public parameters P and Q for Bob and Alice on the same curve
    A_steps = alice_step_public_gen()
    B_steps = bob_steps_public_gen()
    print("Alice steps= ", A_steps)    
    print("Bob steps= ", B_steps)
    return A_steps, B_steps

def bob_private_key_generation():
    E_bob, bob_private_P, bob_private_Q = 0

public_key_generation()