import img_pipeline
import cv2

pl= img_pipeline.img_pipeline(3)

while 1:
	cv2.imshow('noize', pl.product())
	cv2.imshow("img", pl.pdata[0])
	pl.step()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cv2.imwrite("noize.png", pl.product())
cv2.imwrite("img.png", pl.pdata[0])
pl.shutdown()
cv2.destroyAllWindows()
