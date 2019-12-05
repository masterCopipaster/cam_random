import img_pipeline
import cv2

pl= img_pipeline.img_pipeline(5)

while 1:
	cv2.imshow('noize', pl.product())
	pl.step()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
pl.shutdown()
cv2.destroyAllWindows()
