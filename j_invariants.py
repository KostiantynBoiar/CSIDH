from sage.all import *
# Введіть значення простого числа p
p = 121

# Поле Fp2
F = GF(p**2, 'i')
i = F.gen()  # Уявна одиниця

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
    
# Перевірка на суперсингулярність: якщо j-інваріант належить до поля Fp2
def is_supersingular_curve(a, b):
    E = EllipticCurve(F, [a, b])  # Еліптична крива y^2 = x^3 + ax + b
    num_points = E.order()  # Кількість точок на кривій E над F_p
    return num_points == p + 1

def is_singular_curve(a, b):
    # Compute the discriminant: -16(4a^3 + 27b^2)
    discriminant = -16 * (4 * a**3 + 27 * b**2)
    
    # If the discriminant is zero, the curve is singular
    return discriminant == 0

# Function to find valid parameter 'a' for the elliptic curve using consistent values for a and b
def find_valid_a():
    
    points = []  # Stores j-invariant values
    a_params = []  # Stores valid 'a' parameters
    i = 0
    j_count = count_of_j(p)  # Get the number of j-invariants needed
    
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
                a_params.append(a)
                points.append(j)
                print("Supersingular curve detected, j-invariant:", j)
                i += 1  # Increment counter for each valid pair
                
                # Break the loop if the required number of j-invariants is found
                if i >= j_count:
                    return a_params, points

    return a_params, points

# Use the function to find valid 'a' and j-invariant values
a_params, j_invariants = find_valid_a()

# Output the result
print("Знайдені параметри a:", a_params)
print("j-інваріанти кривої:", j_invariants)
