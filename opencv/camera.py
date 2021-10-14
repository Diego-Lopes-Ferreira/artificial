import cv2 as cv

print("Initiating...")

# * Read from Camera
capture = cv.VideoCapture(0)
capture.set(3, 400) # set height
capture.set(3, 600) # set width

while True:
  isTrue, frame = capture.read()
  cv.imshow("Video", frame)
  if cv.waitKey(20) & 0xff == ord('d'):
    break

capture.release()
cv.destroyAllWindows()

print("Ending...")
