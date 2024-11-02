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
    for b in F:
        for a in F:
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
                    print("a param: ", a)
                    print("b param: ", b)
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


# Use the function to find valid 'a' and j-invariant values
params, j_invariants = find_valid_a()
a_param = params[16][0]
b_param = params[16][1]
E = EllipticCurve(F, (a_param, b_param))

# Output the result
print("Знайдені параметри ", params)
print("j-інваріанти кривої:", j_invariants)
print("Count of j-invariants: ", len(j_invariants))

ker_3 = kernel_of_isogeny(E, 3)
ker_2 = kernel_of_isogeny(E, 2)
print(f"Params of the isogeny for the kernel: a = {a_param}, b = {b_param}")
print("Kernel of isogeny [2]ker: ", ker_2)
print("Kernel of isogeny [3]ker: ", ker_3)

print("Curve is supersingular? ", is_supersingular_curve((a_param*ker_3[0][0] - 6 * (ker_3[0][0])**2+6)*ker_3[0][0], b_param))
print("Computed j-invariant for ker[3]: ", j_invariant((a_param*ker_3[0][0] - 6 * (ker_3[0][0])**2+6)*ker_3[0][0], b_param))
print("Curve is supersingular? ", is_supersingular_curve(1802 +3120*i, i))
print("Computed j-invariant for ker[2]: ", j_invariant(1802 +3120*i, i))