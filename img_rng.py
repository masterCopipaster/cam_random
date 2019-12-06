import numpy as np
import random

def line_norm_seq(dif):
	vect = np.linalg.norm(dif, axis = (1,2))
	vect = vect - np.mean(vect)# - min(vect)
	return vect / np.linalg.norm(vect)

def allbytes_seq(dif):
	seq = np.reshape(dif, 640*480*3)
	return seq
	
BASIC_NUMBER = 149

def bit_seq(dif):
	seq = np.reshape(dif, 640*480*3)
	mean = np.sort(seq)[len(seq)//2]
	#print(mean)
	return seq > mean

bitmat = np.array([[1 << j for j in range(32)] for i in range(20 * 480 * 3)]).T 
	
def u32_seq(dif):
	seq = np.reshape(bit_seq(dif), bitmat.shape)
	newseq = np.sum(seq * bitmat, axis = 0)
	#print(newseq.shape)
	return newseq
	
random.seed()

def rand_seq(dif):
	newseq = []
	for i in range(20 * 480 * 3):
		newseq.append(random.randint(0, 0xffffffff))
	return np.array(newseq)	

def file_output(filename, seq):
	file = open(filename, "w")
	file.write("type: d\n")
	file.write("count: " + str(len(seq)) + "\n")
	file.write("numbit: 32\n")
	for num in seq:
		file.write(str(int(num)) + "\n")
