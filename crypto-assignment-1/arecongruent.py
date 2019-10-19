# Anthony Habib - 100662176
# October 4th 2019

# Gets values from user
a = int(input("Enter Value for A:"))
b = int(input("Enter Value for B:"))
n = int(input("Enter Value for N:"))

# Calculates congruency
congruent_A = a % n
congruent_B = b % n

# Checks if A and B are congruent
if congruent_A == congruent_B:
    print("True")
else:
    print("False")

# prints values
print(a, b, n)
