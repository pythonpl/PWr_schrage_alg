import numpy as np
import matplotlib.pyplot as plt
import sys
from queue import PriorityQueue

def main():

	data = np.array
	k = ProcessData(data)

	r = toSingleMatrix(k[:, 0])
	p = toSingleMatrix(k[:, 1])
	q = toSingleMatrix(k[:, 2])

	PI = schrageAlgorithm(r[:], p[:], q[:])

def toSingleMatrix(list):
	result = []

	for i in range(0, len(list)):
		result.append(list[i])
	return result

def ProcessData(data):
    data = np.genfromtxt('SCHRAGE1.DAT',

                     skip_header=1,
                     dtype=int,
                     delimiter="")

    return data

def schrageAlgorithm(r, p, q):
	t = 0
	k = 0
	Cmax = 0

	N = [] 
	N_size = 0
	G = PriorityQueue()
	PI = []

	for i in range(0, len(r)):
		N.append(1);

	N_size = len(N)

	while(not G.empty() or N_size!=0):

		minimum = sys.maxsize
		argmin = -1

		for i in range(0, len(r)):
			if(N[i] == 1 and r[i] < minimum):
				minimum = r[i]
				argmin = i

		while(N_size!=0 and minimum <= t):
			N[argmin] = -1
			N_size-=1
			G.put((-q[argmin], argmin))

			minimum = sys.maxsize

			for i in range(0, len(r)):
				if(N[i] == 1 and r[i] < minimum):
					minimum = r[i]
					argmin = i

		if(G.empty()):
			t = minimum
		else:
			e = G.get()
			PI.append(e[1])

			t+= p[e[1]]

			Cmax = max(Cmax, t+q[e[1]])

	print("Cmax")
	print(Cmax)
	print("Queue: ")
	print(PI)
	return PI

main()