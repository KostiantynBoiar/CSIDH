#sage -python {name_of_the_file.py}
from sage.all import *
# Введіть значення простого числа p
var('i')
p = 241
Fp = GF(p)
S = SupersingularModule(Integer(p))
L,d = S.supersingular_points()
# Define the polynomial ring over Fp with generator x
R = PolynomialRing(Fp, 'x')
x = R.gen()

# Define the irreducible polynomial for the extension
f = x**2 - 3*x + 7

# Define the extension field Fp2 as Fp[x]/(x^2 - 3x + 7)
F = Fp.extension(f, 'a')

def count_of_j(p):
    count = int(p/12)
    mod_p = p % 12
    mod_count = 0
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
    """
    numerator = 256*(a**2-3)**3
    denominator = (a**2-4)
    """
    # Check if the denominator is zero
    if denominator == 0:
        print("Denominator is zero, cannot compute j-invariant for this a, b")
        return None  # or return some default value
    
    answ =  numerator / denominator
    return answ


def j_invariants_over_F(F):
    X = PolynomialRing(F, 'x').gen()

    j_in = supersingular_j(F)
    print(j_in)

    poly = sage.modular.ssmod.ssmod.Phi_polys(2,X,j_in)

    print(poly.roots())

def is_supersingular_curve(j):
    # Define the elliptic curve over Fp2
    return j in L


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
            
            # Compute j-invariant
            j = j_invariant(a, b)
            
            # If j is None, skip to the next iteration
            if j is None:
                continue
            
            # Check if the curve is supersingular
            if is_supersingular_curve(j):

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
    for P in E:
        if n*P==E(0):
            kernel_points.append(P)
    print(len(kernel_points))
    return kernel_points
    


j_invariants_over_F(F)

print(L)
# Use the function to find valid 'a' and j-invariant values
params, j_invariants = find_valid_a()
a_param = params[16][0]
b_param = params[16][1]
E = EllipticCurve(F, (a_param, b_param))
# Output the result
print("Знайдені параметри ", params)
print("j-інваріанти кривої:", j_invariants)
print("Count of j-invariants: ", len(j_invariants))
"""
ker_3 = kernel_of_isogeny(E, 3)
ker_2 = kernel_of_isogeny(E, 2)
print(f"Params of the isogeny for the kernel: a = {a_param}, b = {b_param}")
print("Kernel of isogeny [2]ker: ", ker_2)
print("Kernel of isogeny [3]ker: ", ker_3)
"""

print("kernel of isogeny ", kernel_of_isogeny(E, 5))
#print("Curve is supersingular? ", is_supersingular_curve((a_param*ker_3[0][0] - 6 * (ker_3[0][0])**2+6)*ker_3[0][0], b_param))
#print("Computed j-invariant for ker[3]: ", j_invariant((a_param*ker_3[0][0] - 6 * (ker_3[0][0])**2+6)*ker_3[0][0], b_param))

def find_j_inv_for_particular_curve(a_param, b_param):
    E = EllipticCurve(F, (a_param, b_param))
    for b in F:
        j_inv = j_invariant(a_param, b)
        if j_inv in j_invariants:
            return j_inv
        else: 
            continue
    return -1
