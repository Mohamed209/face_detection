import cv2 as cv
import dlib
img=cv.imread("images/germanyafpgetty.jpg")
# face detector will slide the image to get all faces
fd=dlib.get_frontal_face_detector()
# passing an image to fd object will return bounding boxes coordinates about every detected face
faces=fd(img,1)# 1 to upsample the image so we can detect more faces
print("faces detected {} and their coordinates {}".format(len(faces),faces))
# let us draw a rect on every face and show the image
for face in faces :
    cv.rectangle(img,(face.left(),face.top()),(face.right(),face.bottom()),(0,0,255),2)
    cv.imshow("test",img)
cv.waitKey()