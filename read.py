import cv2 as cv

img = cv.imread('masked.png')
#cv.imshow('speed', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grad', gray)  

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
print(len(faces_rect))


cv.waitKey(3000)
cv.destroyAllWindows()
# ...existing code...