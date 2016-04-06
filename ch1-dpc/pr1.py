import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

#### Given Input
gamma = np.array([1,1.5,1])
G = np.array([[1, 0.1, 0.3], [0.2, 1, 0.3], [0.2, 0.2, 1]])
v = np.array([[0.1],[0.1],[0.1]])
p0 = np.array([[1],[1],[1]])
N = 10

G1 = np.array([[1, 0.1, 0.3, 0.1], [0.2, 1, 0.3, 0.1], [0.2, 0.2, 1, 0.1], [0.1, 0.1, 0.1, 1]])
gamma1 = np.array([1, 1.5, 1, 1])
v1 = np.array([[0.1], [0.1], [0.1], [0.1]])
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
t4 = []
t = []

for i in range(N):
	t1.append(transmit_power[0])
        t2.append(transmit_power[1])
        t3.append(transmit_power[2])
        t4.append(0)
        t.append(i)
	transmit_power = np.dot(np.dot(D, F), transmit_power) + v

t1.append(transmit_power[0])
t2.append(transmit_power[1])
t3.append(transmit_power[2])
t.append(N)

plt.plot(t, t1, 'r^--', t, t2, 'b^--', t, t3, 'g^--')
plt.xlabel('Iterations')
plt.ylabel('Transmt Powers')
plt.title('DPC')
plt.show()

F1 = G1 * np.array([[0,1,1,1], [1,0,1,1], [1,1,0,1],[1,1,1,0]])
D1 = np.array([[gamma1[0], 0, 0, 0], [0, gamma1[1], 0, 0], [0, 0, gamma1[2], 0], [0,0,0,gamma1[3]]])
p10 = np.array([[transmit_power[0]], [transmit_power[1]], [transmit_power[2]], [1]])
transmit_power = p10

t4.append(transmit_power[3])

for i in range(N + 1, 2 * N):
	transmit_power = np.dot(np.dot(D1, F1), transmit_power) + v1
	t1.append(transmit_power[0])
        t2.append(transmit_power[1])
        t3.append(transmit_power[2])
        t4.append(transmit_power[3])
        t.append(i)

plt.plot(t, t1, 'r^--', t, t2, 'b^--', t, t3, 'g^--', t, t4, 'y^--')
plt.xlabel('Iterations')
plt.ylabel('Transmt Powers')
plt.title('DPC-New Tx & Rx')
plt.show()
