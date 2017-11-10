import random

q = int(raw_input("Please enter q : "))
alpha = int(raw_input("Please enter alpha : "))
XA = int(raw_input("Please enter XA : "))
C1 = int(raw_input("please enter C1 : "))
C2 = int(raw_input("please enter C2 : "))


print("(C1,C2) = (" + str(C1) + "," + str(C2) + ")")

K = pow(C1, XA, q)

# compute K's multiplicative inverse mod n using Fermat's little theorem
Km1 = pow(K, q-2, q)

M = C2 * Km1 % q

print("M = " + str(M))
