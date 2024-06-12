import cv2 as cv
#    how to read and show and image
#read a photo

##img = cv.imread("Photos/cat_large.jpg") to read a photo 
# show the video

##cv.imshow('Cat' , img) show the image
##cv.waitKey(0)it will wait an infinite time for a key to be pressed
#   how to read and show and video
#read a video
capture = cv.VideoCapture("Videos/kitten.mp4") # we can put a int if we want to use a camera
while True:
    isTrue , frame =capture.read() # it will readf the video frame by frame and check if it read succ
    cv.imshow('Video', frame)
cv.waitKey(0)
