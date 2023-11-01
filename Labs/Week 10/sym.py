from sympy import Matrix, Eq, solve
from sympy.abc import N, P, m, c, K
import numpy as np

VARS = Matrix([N, P])

dNdt = [N*(1-N/K) - P*(m*N/(1+N))]
dPdt = [-c*P + P*(m*N/(1+N))] 

M = Matrix([dNdt, dPdt])

D = M.jacobian(VARS)
print("Matrix:", M)
print("Derivative", D)

# Now let's find the equilibrium points and evaluate the jacobian there.

eq1 = Eq(dNdt[0], 0)
eq2 = Eq(dPdt[0], 0)

equilibriums = solve((eq1, eq2), (N,P))
print("Equilibrium points:", equilibriums)

matrix_of_rates = Matrix([dNdt[0], dPdt[0]])
for e in equilibriums:
	A = D.subs(N,e[0])
	B = A.subs(P, e[1])
	print(B)