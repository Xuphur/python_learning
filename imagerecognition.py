import cv2 as cv

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv.CascadeClassifier(alg)
file_name = "test-image.jpg"

img = cv.imread(file_name)
gray_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
faces = haar_cascade.detectMultiScale(
  gray_img, scaleFactor=1.05, minNeighbors=5, minSize=(100,100)
)

i=0
for x,y,w,h in faces:
  cropped_image = img[y:y+h,x:x+w]
  target_file = 'stored_faces/'+str(i)+'.jpg'
  cv.imwrite(
    target_file,
    cropped_image,
  )
  i = i+1