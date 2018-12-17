import cv2
import numpy as np
import urllib.request
with urllib.request.urlopen("http://192.168.43.1:8080/shot.jpg") as url:
	print("success")
while True:
	imgNp=np.array(bytearray(url.read()), dtype=np.uint8)
	img=cv2.imdecode(imgNp,-1)
	cv2.imshow('test',img)
	if ord('q')==cv2.waitKey(10):
		exit(0)