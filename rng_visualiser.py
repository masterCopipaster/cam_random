import numpy as np
import cv2
import matplotlib.pyplot as plt
import img_pipeline
import img_rng

pl= img_pipeline.img_pipeline(3)
vector = np.array([])

while(True):
	img = pl.product()
	cv2.imshow('noize', img)
	vector = np.concatenate((vector, img_rng.u32_seq(img)))
	pl.step()

	hist, bins = np.histogram(vector, bins=50)
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
#img_rng.file_output("dataout.txt", vector)
pl.shutdown()
cv2.destroyAllWindows()

