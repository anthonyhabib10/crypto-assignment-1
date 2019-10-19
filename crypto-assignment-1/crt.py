# Anthony Habib - 100662176
# October 4th 2019

from sympy.ntheory.modular import crt
from numpy import gcd

# gets value from user input
a = int(input("Enter a Value for A:"))
b = int(input("Enter a Value for B:"))
c = int(input("Enter a Value for C:"))
r = int(input("Enter a Value for R:"))
s = int(input("Enter a Value for S:"))
t = int(input("Enter a Value for T:"))

# Checks for relatively prime
if gcd(r,s) == gcd(s,t) == gcd(r,t) != 1:
    print("They are not relatively prime")

# calculates the Chinese remainder theorem
list_congruencies = []
num = crt([a, b, c], [r, s, t])
for x in num:
    list_congruencies.append(x)
print("The congruency for x is:", list_congruencies)
