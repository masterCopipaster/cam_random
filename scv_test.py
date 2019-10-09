import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

while(True):
	frame1 = frame
	ret, frame = cap.read()
	dif = frame - frame1
    	cv2.imshow('frame', dif)
	vector = np.linalg.norm(dif, axis = (1,2))
	transform = np.abs(np.fft.fft(vector))
	plt.plot(transform[1:])
	plt.savefig('gr.png')
	gr = cv2.imread('gr.png')
	cv2.imshow('graph', gr)
	plt.cla()
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


