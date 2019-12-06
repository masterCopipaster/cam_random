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

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
img_rng.file_output("dataout.txt", vector)
pl.shutdown()
cv2.destroyAllWindows()
