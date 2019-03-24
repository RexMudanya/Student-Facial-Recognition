#main working face detector
import cv2
import numpy as np
import os
from pymongo import MongoClient
import datetime
import pprint


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingData.xml")
id=0
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
fontface=cv2.FONT_HERSHEY_SIMPLEX
fontscale=1
fontcolor=(255,255,255)

'''
def getProfile(id):
	conn=sqlite3.connect("/home/rex/sqlitestudio-3.2.1/SQLiteStudio/FaceBase")
	params=(id,name)
	cmd="SELECT * FROM People WHERE ID="+str(id)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close()
	return profile
	'''
def getNm(id):
	if (id==1):
		id="Rex"
	elif(id==2):
		id=="Angulu"
	elif(id==3):
		id="Omoi"
	else:
		id=id

	return id

def getProfile(id):
	client=MongoClient('localhost',27017)
	db=client['FaceRecBase']
	collection=db['credentials']
	posts=db.posts

	return posts.find_one({"id":id},{id: 1, name:1})


while True:
	ret,img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		id, conf = recognizer.predict(gray[y:y+h,x:x+w])
		
		#id=getNm(id)
		print(conf)
		if(conf==0):
			cv2.putText(img,"matches",(x,y+h+30),fontface,fontscale,(255,255,255))
		cv2.putText(img,str(id),(x,y+h+50),fontface,fontscale,(255,255,255))
	cv2.imshow("Face",img)
	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
