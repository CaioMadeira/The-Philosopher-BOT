import cv2

face_cascade = cv2.CascadeClassifier('face.xml')

img = cv2.imread('fel.jpg')


faces = face_cascade.detectMultiScale(img, 1.1, 4)

print(faces)
get = False
for a in faces:
  ver = all(a)
  if ver == True:
    get = True
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 10)
    cv2.imwrite("face_detected.png", img)
    print('Successfully saved')


if get == True:
  print('ACHOU ROSTO')

else:
  print('NUM ACHEI NADA NAO FI')

