import cv2
import face_recognition
import numpy as np

#taking input pictures
img1=cv2.imread("WIN_20220322_12_50_53_Pro.jpg")
img2=cv2.imread("WIN_20220322_20_53_31_Pro.jpg")

#converting BGR to RGB
rgb1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
rgb2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

#finding face encodings
encodings1=face_recognition.face_encodings(rgb1)[0]
encodings2=face_recognition.face_encodings(rgb2)[0]

face_distances=face_recognition.face_distance([encodings1],encodings2)

face_match_percentage = (1-face_distances)*100
if face_distances<=0.5:
    print('2 faces perfectly matched')
elif face_distances<=0.6:
    print('2 faces matched')
else:
    print("2 faces didn't matched")
print ("percent matching: ",float(np.round(face_match_percentage,4)),'%') #upto 4 decimal places
