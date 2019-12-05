import cv2 as cv

class img_pipeline :
	plen = 3
	cap = None
	pdata = None
	
	def __init__(self, _plen = None, _cap = cv.VideoCapture(0)):
		if _plen:
			self.plen = _plen
		self.cap = _cap
		self.pdata = [self.cap.read()[1] for i in range(self.plen)] 
		
		
	def step(self, img = None):
		if not img: 
			ret, img = self.cap.read()
		self.pdata = [img] + self.pdata[:-1]
		
	def product(self):
		return sum(self.pdata[0] - frame for frame in self.pdata[-1:]) ** 3
		
	def shutdown(self):
		self.cap.release()
		
