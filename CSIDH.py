from j_invariants import *
import random


def public_params_generator(param):
    """Generate a supersingular curve and return public parameters."""
    for b in F:
        E = EllipticCurve(F, (param[1], b))
        j_inv_of_E = j_invariant(param[1], b)
        if is_supersingular_curve(j_inv_of_E):
            # Generate two independent points on the same supersingular curve
            P = E.random_point()  # First point
            Q = E.random_point()  # Second point, independent of P
            return E, P, Q  # Return the curve and the two points
    return None, None, None

def private_key_generation():
    # Generate public parameters P and Q for Bob and Alice on the same curve
    E_bob, bob_public_p, bob_public_q = public_params_generator(choice(params))
    E_alice, alice_public_p, alice_public_q = public_params_generator(choice(params))
    
    # Check if valid public parameters are generated
    if not (E_alice and alice_public_p and alice_public_q):
        print("Error: Failed to generate valid public parameters for Alice.")
        return None
    
    print("Bob's public parameters: P_B =", bob_public_p, ", Q_B =", bob_public_q)
    print("Alice's public parameters: P_A =", alice_public_p, ", Q_A =", alice_public_q)
    
    # Alice's secret scalar
    k_A = 11
    
    # Perform scalar multiplication [k_A]Q_A on Alice's curve
    kA_QA = k_A * alice_public_q  # This calculates [k_A]Q_A on the same curve E_alice
    
    # Compute S_A as the sum of P_A and [k_A]Q_A, both on the curve E_alice
    S_a = alice_public_p + kA_QA  # Calculate S_A = P_A + [k_A]Q_A
    
    print("S_a parameter:", S_a)
    return S_a

private_key_generation()