'''
	using IP Webcam app 
1.ensure pc and mobile on the sam network 
2.start server on mobile app
3.copy url from mobile into browser
4.select javascript for video
5.right click on the video stream 
6.select copy image location 
7.paste into url
'''

import urllib.request
import cv2
import numpy as np

url='http://192.168.43.1:8080/shot.jpg?rnd=505926'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('test',img)
    
    if(cv2.waitKey(1)==ord('q')):
       break
