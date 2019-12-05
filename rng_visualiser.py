import numpy as np
import cv2
import matplotlib.pyplot as plt
import img_pipeline
import img_rng

pl= img_pipeline.img_pipeline(5)

while(True):
	vector = img_rng.line_norm_seq(pl.product())
	pl.step()

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
pl.shutdown()
cv2.destroyAllWindows()

