import random

q = 67
alpha = 12

# a<= randint(a,b) <= b  
XA = random.randint(2, q-2)

# python has built-in power with mod function
YA = pow(alpha, XA, q)

print("private key : " + str(XA))
print("public key (q, alpha, Ya) : (" + str(q)  + ", " + str(alpha) + ", " + str(YA) + ")")