"""
	code creates a dataset of images to be trained by opening camera and capturing
	20 images of a detected face 
	also takes input of user id and name of persons face and inserts into a database
"""
import cv2
import numpy as np
import os
import sqlite3
import importlib
"""
moduleName='mongoEnd.py'
importlib.import_module(moduleName)
"""

def insertOrUpdate(Id, Name):
	conn =sqlite3.connect("/home/rex/sqlitestudio-3.2.1/SQLiteStudio/FaceBase")
	params = (id,name)
	#cmd="SELECT * FROM People WHERE ID="+str(Id)
	#cursor=conn.execute(cmd,params)
	c=conn.cursor()

	conn.execute('''SELECT * FROM People WHERE ID='''+str(Id))
	isRecordExist=0
	for row in c.execute.execute('''SELECT * FROM People WHERE ID='''+str(Id)):
		isRecordExist=1
	if(isRecordExist==1):
		#cmd="UPDATE People SET NAME="+str(Name)+" WHERE ID="+str(Id)
		conn.execute('''UPDATE People SET NAME='''+str(Name)+'''WHERE ID='''+str(id))
	else:
		#cmd="INSERT INTO People (ID,NAME) VALUES("+str(Id)+","+str(Name)+")"
		conn.execute('''INSERT INTO People VALUES('''+str(Id)+''','''+str(Name)+''')''')
	#conn.execute(cmd,params)
	conn.commit()
	conn.close()

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

id=input('enter user id ')
name=input('enter your name ')

insertOrUpdate(id,name)

sampleNum=0

while True:
	ret,img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		sampleNum+=1
		cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.waitKey(100)
	cv2.imshow("Face",img)
	cv2.waitKey(1)
	if(sampleNum>20):
		break

cam.release()
cv2.destroyAllWindows()