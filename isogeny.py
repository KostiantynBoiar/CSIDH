from sage.all import *

# Define the given coefficient for the elliptic curve E_a
a = 115 * I + 190
E_a = EllipticCurve([0, 0, 0, a, 1])  # Define the elliptic curve E_a: y^2 = x^3 + ax^2 + x

# Step 1: Find possible values of alpha for points of order 2 on the curve
# Define the polynomial for finding alpha
x = var('x')
alpha_polynomial = x**3 + a * x**2 + x
alpha_solutions = alpha_polynomial.roots(multiplicities=False)

# Select a non-zero root as alpha (ignoring trivial solution alpha = 0)
alpha = None
for solution in alpha_solutions:
    if solution != 0:
        alpha = solution
        break

if alpha is None:
    print("No suitable alpha found for kernel. Adjust input values.")
else:
    # Step 2: Compute the new coefficient a' for the isogenous curve E_a'
    a_prime = 2 * (1 - 2 * alpha**2)
    E_a_prime = EllipticCurve([0, 0, 0, a_prime, 1])  # Define the new curve E_a'

    # Step 3: Define the isogeny map φ from E_a to E_a'
    def isogeny_map(x_val):
        return x_val * (alpha * x_val - 1) / (x_val - alpha)

    # Display the results
    print("Original Curve E_a:", E_a)
    print("New Curve E_a' after 2-isogeny:", E_a_prime)
    print("Chosen kernel point α:", alpha)
    print("Isogeny map φ(x) =", isogeny_map(x))
