import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

def seq_generate(dif):
	vect = np.linalg.norm(dif, axis = (1,2))
        return vect

vector = np.array([])
while(True):
	for i in range(2):
		vector = np.array([])
		frame1 = frame
		ret, frame = cap.read()
		dif = frame - frame1
		dif = dif ** 3 #- dif ** 2 + dif
		cv2.imshow("noize", dif)
		vector = np.concatenate((vector, seq_generate(dif)))

	hist, bins = np.histogram(vector, bins=20)
	width = 0.7 * (bins[1] - bins[0])
	center = (bins[:-1] + bins[1:]) / 2
	plt.bar(center, hist, align='center', width=width)
	plt.savefig('gr.png')
	gr = cv2.imread('gr.png')
	cv2.imshow('graph', gr)
	plt.cla()
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

