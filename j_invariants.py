#sage -python {name_of_the_file.py}
from sage.all import *
# Введіть значення простого числа p
p = 241

# Поле Fp2
F = GF(p**2, 'i')
i = F.gen()  # Уявна одиниця
CC = ComplexField(100)

def count_of_j(p):
    count = int(p/12)
    mod_p = p % 12
    mod_count = 0
    answ = 0
    if mod_p == 1:
       mod_count = 0
    elif mod_p == 5 or mod_p == 7:
        mod_count = 1
    elif mod_p == 11:
        mod_count = 2
    else:
        return 0
    return count + mod_count
    
    
def j_invariant(a, b):
    numerator = 1728 * (4 * a**3)
    denominator = 4 * a**3 + 27 * b**2
    
    # Check if the denominator is zero
    if denominator == 0:
        print("Denominator is zero, cannot compute j-invariant for this a, b")
        return None  # or return some default value
    
    answ = numerator / denominator
    return answ
    
def is_supersingular_curve(a, b):
    # Define the elliptic curve over Fp2
    E = EllipticCurve(F, [a, b])  # Elliptic curve y^2 = x^3 + ax + b over Fp2
    
    # Use SageMath's built-in function to check if the curve is supersingular
    return E.is_supersingular()


def is_singular_curve(a, b):
    # Compute the discriminant: -16(4a^3 + 27b^2)
    discriminant = -16 * (4 * a**3 + 27 * b**2)
    
    # If the discriminant is zero, the curve is singular
    return discriminant == 0

# Function to find valid parameter 'a' for the elliptic curve using consistent values for a and b
def find_valid_a():
    
    points = []  # Stores CC = ComplexField(100)j-invariant values
    i = 0
    j_count = count_of_j(p)  # Get the number of j-invariants needed
    params = []
    # Iterate over all possible values of 'a' and 'b' in the field Fp2
    for a in F:
        for b in F:
            # Check if the curve is singular
            if is_singular_curve(a, b):
                print("Singular curve detected, skipping this pair.")
                continue
            
            # Compute j-invariant
            j = j_invariant(a, b)
            
            # If j is None, skip to the next iteration
            if j is None:
                continue
            
            # Check if the curve is supersingular
            if is_supersingular_curve(a, b):

                if j not in points:
                    a_b_params = a, b
                    params.append(a_b_params)
                    points.append(j)
                    print("Supersingular curve detected, j-invariant:", j)
                    i += 1  # Increment counter for each valid pair
                
                # Break the loop if the required number of j-invariants is found
                if i >= j_count:
                    return params, points

    return params, points


def kernel_of_isogeny(E, n):

    kernel_points = []
    
    # Iterate through points on E to find those with order dividing n
    for P in E:
        if P.order() == n:
            kernel_points.append(P.xy())  # Append the point's coordinates

    return kernel_points


    
def j_invariant_param():
    # Define the complex parameter in the expression
    complex_term = CC(sqrt(43700 * I + 22871) + 115 * I + 190)
    
    # Compute the coefficient a = 2 - complex_term^2
    a = 2 - complex_term**2
    b = 1  # As per your equation, the constant term with x is simply 'x'

    # Define the elliptic curve
    E = EllipticCurve([a, b])

    # Check if the curve is singular
    if is_singular_curve(a, b):
        print("The curve is singular for the given parameter.")
        return None

    # Compute the j-invariant
    j = j_invariant(a, b)
    return j

# Example usage



j_value = j_invariant_param()
print("Computed j-invariant:", j_value)


# Use the function to find valid 'a' and j-invariant values
params, j_invariants = find_valid_a()
E = EllipticCurve(F, (params[0][0], params[0][1]))

# Output the result
print("Знайдені параметри a:", params)
print("Знайдені параметри b:", params[1][0])
print("j-інваріанти кривої:", j_invariants)
print("Count of j-invariants: ", len(j_invariants))

print("Kernel of isogeny: ", kernel_of_isogeny(E, 2))
