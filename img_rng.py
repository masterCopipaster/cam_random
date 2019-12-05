import numpy as np

def line_norm_seq(dif):
	vect = np.linalg.norm(dif, axis = (1,2))
	return vect

def allbytes_seq(dif):
	return np.reshape(dif, 640*480*3)
