import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

#### Given Input
gamma = np.array([1,2,1])
G = np.array([[1, 0.5, 0.5], [0.5, 1, 0.5], [0.5, 0.5, 1]])
v = np.array([[0.1],[0.1],[0.1]])
p0 = np.array([[1],[1],[1]])
N = 20 

####

#####
#   p(t+1) = D * F * p(t) + v
#####

F = G * np.array([[0,1,1], [1,0,1], [1,1,0]])
D = np.array([[gamma[0], 0, 0], [0, gamma[1], 0], [0, 0, gamma[2]]])
transmit_power = p0

t1 = []
t2 = []
t3 = []
t = []

for i in range(N):
	t1.append(transmit_power[0])
        t2.append(transmit_power[1])
        t3.append(transmit_power[2])
        t.append(i)
	transmit_power = np.dot(np.dot(D, F), transmit_power) + v

t1.append(transmit_power[0])
t2.append(transmit_power[1])
t3.append(transmit_power[2])
t.append(N)

#plt.plot(t, t1, 'r^--', t, t2, 'b^--', t, t3, 'g^--')
#plt.xlabel('Iterations')
#plt.ylabel('Transmt Powers')
#plt.title('DPC')
#plt.show()
