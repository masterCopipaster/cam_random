import numpy as np

def line_norm_seq(dif):
	vect = np.linalg.norm(dif, axis = (1,2))
	vect = vect - np.mean(vect)# - min(vect)
	return vect / np.linalg.norm(vect)

def allbytes_seq(dif):
	return np.reshape(dif, 640*480*3)

def file_output(filename, seq):
	file = open(filename, "w")
	file.write("type: d\n")
	file.write("count: " + str(len(seq)) + "\n")
	file.write("numbit: 32\n")
	for num in seq:
		file.write(str(int(num * 0xFFFFFFFF)) + "\n")
