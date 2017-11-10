import random

q = int(raw_input("Please enter q : "))
alpha = int(raw_input("Please enter alpha : "))
YA = int(raw_input("Please enter YA : "))
plaintext = int(raw_input("Please enter plaintext value to encrypt : (1 < M < q-1) "))

k = random.randint(2, q-2)

K = pow(YA, k, q)

C1 = pow(alpha, k, q)
C2 = (K * plaintext) % q

print("(C1,C2) = (" + str(C1) + "," + str(C2) + ")")
