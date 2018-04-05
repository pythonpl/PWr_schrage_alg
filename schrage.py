import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

def main():

	data = np.array
	r = [2, 3, 6, 10, 15]
	p = [3, 2, 2, 1, 1]
	q = [5, 4, 2, 1, 1]	
	
	k = ProcessData(data)
	r = toSingleMatrix(k[:, 0])
	p = toSingleMatrix(k[:, 1])
	q = toSingleMatrix(k[:, 2])	

	visualize(r, p, q)

def visualize(r, p, q):

	results = schrageAlgorithm(r[:], p[:], q[:])
	queue = results[0]
	Cmax = results[1]

	stack = r[queue[0]]+p[queue[0]]
	offset = []
	for i in range(0, len(queue)):
		offset.append(0)
	offset[queue[0]] = 0
	for i in range (1, len(queue)):
		e = stack - r[queue[i]]
		int(e)
		if(e>=0):
			offset[queue[i]] = e
			stack = stack + p[queue[i]]
		else:
			offset[queue[i]] = 0
			stack = stack - e + p[queue[i]]
	
	plt.rcdefaults()
	fig = matplotlib.pyplot.gcf()
	fig.set_size_inches(17, 8)		
	N = len(r)
	ind = np.arange(N)
	width = 0.4
	
	order = getCorrectGraphOrder(r, p, q, queue, offset, 1)
	
	r_ = order[0]
	p_ = order[1]
	q_ = order[2]
	offset_ = order[3]
	queue_ = order[4]

	p1 = plt.barh(ind, offset_, width, color='w')
	p2 = plt.barh(ind, r_, width, left=offset_, color='gray')
	p3 = plt.barh(ind, p_, width, left=np.array(offset_)+np.array(r_), color='r')
	p4 = plt.barh(ind, q_, width, left=np.array(offset_)+np.array(r_)+np.array(p_), color='k')
	
	plt.legend((p1[0], p2[0], p3[0], p4[0]), ("Idle", "Release", "Process", "Delivery"), framealpha=1)
	plt.ylabel("Order: "+str(queue_))
	plt.yticks([])
	plt.ylim([-width/2,len(r)-1+width/2])
	plt.xlim([0, Cmax])
	plt.show()

def getCorrectGraphOrder(r, p, q, queue, offset, option):
	if option == 0:
		queue_ = []		
		for i in range(0, len(r)):
			queue_.append(i)
		return [r, p, q, offset, queue_]
	
	r_=[]
	p_=[]
	q_=[]
	offset_=[]

	for i in range(0, len(r)):
		r_.append(r[queue[i]])
		p_.append(p[queue[i]])
		q_.append(q[queue[i]])
		offset_.append(offset[queue[i]])

	

	return [r_, p_, q_, offset_, queue]
	
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
	G = []
	PI = []

	for i in range(0, len(r)):
		N.append(1);

	N_size = len(N)

	while(len(G)!=0 or N_size!=0):

		minimum = sys.maxsize
		argmin = -1

		for i in range(0, len(r)):
			if(N[i] == 1 and r[i] < minimum):
				minimum = r[i]
				argmin = i

		while(N_size!=0 and minimum <= t):
			N[argmin] = -1
			N_size-=1
			G.append((q[argmin], argmin))

			minimum = sys.maxsize

			for i in range(0, len(r)):
				if(N[i] == 1 and r[i] < minimum):
					minimum = r[i]
					argmin = i

		if(len(G)==0):
			t = minimum
		else:
			maximum = -1
			maxID = -1  
			ind = -1
			for i in range(0, len(G)):
				A = G[i]
				#print "A: "+str(A[0])+" "+str(A[1])
				if maximum<A[0]:
					maximum = A[0]
					maxID = A[1]
					ind = i

			G.remove(G[ind])
			#print "Adding to PI: ("+str(maximum)+", "+str(maxID)+")"
			PI.append(maxID)

			t+= p[maxID]

			Cmax = max(Cmax, t+q[maxID])

	#print "Cmax: "+str(Cmax)
	#print "Queue: "
	print("Cmax: "+str(Cmax))
	print(PI)
	return (PI, Cmax)

main()